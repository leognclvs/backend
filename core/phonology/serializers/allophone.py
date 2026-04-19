from rest_framework import serializers
from core.phonology.models import Allophone


class AllophoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allophone
        fields = [
            "id",
            "phoneme",
            "ipa",
            "environment",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]