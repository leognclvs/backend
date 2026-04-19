from rest_framework import serializers
from core.corpus.models import ExampleSentenceWord


class ExampleSentenceWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleSentenceWord
        fields = [
            "id",
            "example_sentence",
            "position",
            "surface_form",
            "lexeme",
            "gloss",
            "grammatical_info",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]