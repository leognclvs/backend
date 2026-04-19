from rest_framework import serializers
from core.lexicon.models import LexemeSense


class LexemeSenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = LexemeSense
        fields = [
            "id",
            "lexeme",
            "sense_number",
            "definition",
            "semantic_domain",
            "connotation",
            "usage_context",
            "taboo_level",
            "figurative",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]