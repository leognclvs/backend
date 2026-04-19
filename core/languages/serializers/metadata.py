from rest_framework import serializers
from core.languages.models import LanguageMetadata


class LanguageMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageMetadata
        fields = [
            "id",
            "fictional_region",
            "real_world_influences",
            "cultural_notes",
            "historical_notes",
            "phonological_notes",
            "grammatical_notes",
            "estimated_speakers",
            "difficulty_level",
            "tags",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]