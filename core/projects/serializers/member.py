from rest_framework import serializers

from core.projects.models import ProjectMember


class ProjectMemberSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source="user.email", read_only=True)
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = ProjectMember
        fields = [
            "id",
            "user",
            "user_email",
            "username",
            "role",
            "can_edit",
            "can_delete",
            "can_invite",
            "joined_at",
        ]
        read_only_fields = ["id", "joined_at", "user_email", "username"]