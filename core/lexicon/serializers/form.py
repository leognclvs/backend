from rest_framework import serializers
from core.lexicon.models import LexemeForm


class LexemeFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = LexemeForm
        fields = [
            "id",
            "lexeme",
            "form",
            "form_type",
            "phonological_form",
            "orthographic_form",
            "grammatical_signature",
            "is_irregular",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]