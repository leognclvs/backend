from rest_framework import serializers
from core.accounts.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "id",
            "bio",
            "avatar",
            "preferred_language",
            "timezone",
            "public_visibility",
            "website",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]