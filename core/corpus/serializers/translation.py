from rest_framework import serializers
from core.corpus.models import Translation


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = [
            "id",
            "language",
            "source_text",
            "target_text",
            "source_language_name",
            "target_language_name",
            "translation_type",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]