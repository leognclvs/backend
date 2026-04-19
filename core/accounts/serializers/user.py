from copy import deepcopy

from rest_framework import serializers

from core.accounts.models import Profile, User

DEFAULT_PREFERENCES = {
    "theme": "system",
    "language": "pt-BR",
    "notifications_email": True,
    "notifications_push": False,
    "notify_mentions": True,
    "notify_project_updates": True,
    "notify_security_alerts": True,
    "notification_digest": "daily",
    "profile_visibility": "members",
    "activity_visibility": "members",
    "allow_search_indexing": False,
    "share_presence": True,
    "export_format": "pdf",
    "export_scope": "project",
    "export_include_ipa": True,
    "export_include_etymology": True,
    "export_include_examples": True,
}


def build_preferences(profile: Profile | None):
    preferences = deepcopy(DEFAULT_PREFERENCES)

    if not profile:
        return preferences

    preferences.update(profile.preferences or {})
    preferences["language"] = profile.preferred_language or preferences["language"]
    preferences["profile_visibility"] = (
        "public" if profile.public_visibility else "members"
    )
    return preferences


class UserSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    plan = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(source="date_joined", read_only=True)
    email_verified = serializers.BooleanField(source="is_verified", read_only=True)
    preferences = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "display_name",
            "avatar_url",
            "bio",
            "role",
            "plan",
            "created_at",
            "updated_at",
            "email_verified",
            "preferences",
        ]

    def get_avatar_url(self, obj):
        profile = getattr(obj, "profile", None)
        return getattr(profile, "avatar", "") or ""

    def get_bio(self, obj):
        profile = getattr(obj, "profile", None)
        return getattr(profile, "bio", "") or ""

    def get_role(self, obj):
        if obj.is_superuser or obj.is_staff:
            return "admin"
        return "free"

    def get_plan(self, obj):
        return "free"

    def get_preferences(self, obj):
        return build_preferences(getattr(obj, "profile", None))


class UserUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, max_length=50)
    display_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    bio = serializers.CharField(required=False, allow_blank=True)
    avatar_url = serializers.CharField(required=False, allow_blank=True)
    preferences = serializers.DictField(required=False)

    def validate_username(self, value):
        username = value.strip().lower()
        qs = User.objects.filter(username=username)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("Já existe um usuário com este username.")
        return username

    def update(self, instance, validated_data):
        profile, _ = Profile.objects.get_or_create(user=instance)

        if "username" in validated_data:
            instance.username = validated_data["username"]

        if "display_name" in validated_data:
            instance.display_name = validated_data["display_name"].strip()

        if "bio" in validated_data:
            profile.bio = validated_data["bio"].strip()

        if "avatar_url" in validated_data:
            profile.avatar = validated_data["avatar_url"].strip()

        if "preferences" in validated_data:
            incoming_preferences = validated_data["preferences"] or {}
            merged_preferences = build_preferences(profile)
            merged_preferences.update(incoming_preferences)

            profile.preferences = merged_preferences
            profile.preferred_language = merged_preferences.get("language", profile.preferred_language)
            profile.public_visibility = merged_preferences.get("profile_visibility") == "public"

        instance.save()
        profile.save()
        return instance


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    display_name = serializers.CharField(required=False, allow_blank=True, max_length=100)

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "display_name",
            "password",
            "password_confirm",
        ]

    def validate(self, data):
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError("As senhas não coincidem.")
        return data

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        display_name = validated_data.pop("display_name", "").strip()

        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
            display_name=display_name,
        )
        Profile.objects.get_or_create(user=user)
        return user
