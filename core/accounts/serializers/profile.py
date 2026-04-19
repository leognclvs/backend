from rest_framework import serializers
from core.accounts.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    avatar_url = serializers.CharField(source="avatar", required=False, allow_blank=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "bio",
            "avatar",
            "avatar_url",
            "preferred_language",
            "timezone",
            "public_visibility",
            "website",
            "preferences",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
