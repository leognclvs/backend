from rest_framework import serializers

from core.projects.models import Project, ProjectMember
from .member import ProjectMemberSerializer


class ProjectReadSerializer(serializers.ModelSerializer):
    owner_email = serializers.EmailField(source="owner.email", read_only=True)
    members = ProjectMemberSerializer(many=True, read_only=True)

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
            "created_at",
            "updated_at",
            "members",
        ]
        read_only_fields = fields


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