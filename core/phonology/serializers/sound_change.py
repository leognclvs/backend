from rest_framework import serializers
from core.phonology.models import SoundChangeRule


class SoundChangeRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundChangeRule
        fields = [
            "id",
            "language",
            "name",
            "input_pattern",
            "output_pattern",
            "environment",
            "order",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]