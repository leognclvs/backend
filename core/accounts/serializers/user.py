from copy import deepcopy

from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
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


def get_safe_profile(user: User) -> Profile | None:
    try:
        return user.profile
    except (AttributeError, ObjectDoesNotExist, DatabaseError):
        # Evita quebrar o payload de auth quando o perfil ainda nao existe
        # ou quando o schema do banco nao foi migrado por completo.
        return None


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
        profile = get_safe_profile(obj)
        return getattr(profile, "avatar", "") or ""

    def get_bio(self, obj):
        profile = get_safe_profile(obj)
        return getattr(profile, "bio", "") or ""

    def get_role(self, obj):
        if obj.is_superuser or obj.is_staff:
            return "admin"
        return "free"

    def get_plan(self, obj):
        return "free"

    def get_preferences(self, obj):
        return build_preferences(get_safe_profile(obj))


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
            raise serializers.ValidationError("Ja existe um usuario com este username.")
        return username

    def validate_display_name(self, value):
        return value.strip()

    def validate_bio(self, value):
        return value.strip()

    def validate_avatar_url(self, value):
        return value.strip()

    def update(self, instance, validated_data):
        profile, _ = Profile.objects.get_or_create(user=instance)
        user_update_fields = []
        profile_update_fields = []

        if "username" in validated_data:
            instance.username = validated_data["username"]
            user_update_fields.append("username")

        if "display_name" in validated_data:
            instance.display_name = validated_data["display_name"]
            user_update_fields.append("display_name")

        if "bio" in validated_data:
            profile.bio = validated_data["bio"]
            profile_update_fields.append("bio")

        if "avatar_url" in validated_data:
            profile.avatar = validated_data["avatar_url"]
            profile_update_fields.append("avatar")

        if "preferences" in validated_data:
            incoming_preferences = validated_data["preferences"] or {}
            merged_preferences = build_preferences(profile)
            merged_preferences.update(incoming_preferences)

            profile.preferences = merged_preferences
            profile.preferred_language = merged_preferences.get(
                "language", profile.preferred_language
            )
            profile.public_visibility = (
                merged_preferences.get("profile_visibility") == "public"
            )
            profile_update_fields.extend(
                ["preferences", "preferred_language", "public_visibility"]
            )

        if user_update_fields:
            user_update_fields.append("updated_at")
            instance.save(update_fields=list(dict.fromkeys(user_update_fields)))

        if profile_update_fields:
            profile_update_fields.append("updated_at")
            profile.save(update_fields=list(dict.fromkeys(profile_update_fields)))

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
            raise serializers.ValidationError("As senhas nao coincidem.")
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
