from rest_framework import serializers
from core.phonology.models import SyllablePattern


class SyllablePatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = SyllablePattern
        fields = [
            "id",
            "language",
            "pattern",
            "is_common",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]