from django.utils.text import slugify
from rest_framework import serializers

from core.projects.models import Project, ProjectMember
from .member import ProjectMemberSerializer


class ProjectReadSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    owner_email = serializers.EmailField(source="owner.email", read_only=True)
    members = ProjectMemberSerializer(many=True, read_only=True)
    members_count = serializers.SerializerMethodField()
    languages_count = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    archived = serializers.BooleanField(source="is_archived", read_only=True)
    current_user_role = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id",
            "owner",
            "owner_email",
            "name",
            "slug",
            "description",
            "visibility",
            "status",
            "is_archived",
            "archived",
            "members_count",
            "languages_count",
            "current_user_role",
            "tags",
            "created_at",
            "updated_at",
            "members",
        ]
        read_only_fields = fields

    def get_owner(self, obj):
        return {
            "id": str(obj.owner_id),
            "username": obj.owner.username,
            "display_name": obj.owner.display_name or obj.owner.username,
            "avatar_url": getattr(getattr(obj.owner, "profile", None), "avatar", ""),
        }

    def get_members_count(self, obj):
        return obj.members.count()

    def get_languages_count(self, obj):
        return obj.languages.count()

    def get_tags(self, obj):
        return []

    def get_current_user_role(self, obj):
        request = self.context.get("request")
        if not request or request.user.is_anonymous:
            return None
        if obj.owner_id == request.user.id:
            return "owner"

        membership = obj.members.filter(user=request.user).first()
        if not membership:
            return None
        return "editor" if membership.role == "admin" else membership.role


class ProjectWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "visibility",
            "status",
            "is_archived",
        ]
        read_only_fields = ["id"]
        extra_kwargs = {
            "slug": {"required": False, "allow_blank": True},
            "status": {"required": False},
            "is_archived": {"required": False},
        }

    def validate_slug(self, value):
        value = value.strip().lower()
        qs = Project.objects.filter(slug=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError("Já existe um projeto com este slug.")

        return value

    def create(self, validated_data):
        request = self.context["request"]
        if not validated_data.get("slug"):
            base_slug = slugify(validated_data["name"])[:40] or "projeto"
            candidate = base_slug
            counter = 2
            while Project.objects.filter(slug=candidate).exists():
                candidate = f"{base_slug}-{counter}"
                counter += 1
            validated_data["slug"] = candidate

        validated_data.setdefault("status", "active")
        validated_data.setdefault("is_archived", False)
        project = Project.objects.create(owner=request.user, **validated_data)

        ProjectMember.objects.create(
            project=project,
            user=request.user,
            role="owner",
            can_edit=True,
            can_delete=True,
            can_invite=True,
        )
        return project
