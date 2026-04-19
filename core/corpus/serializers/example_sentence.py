from rest_framework import serializers

from core.corpus.models import ExampleSentence
from .example_word import ExampleSentenceWordSerializer


class ExampleSentenceReadSerializer(serializers.ModelSerializer):
    words = ExampleSentenceWordSerializer(many=True, read_only=True)

    class Meta:
        model = ExampleSentence
        fields = [
            "id",
            "language",
            "text_native",
            "text_romanized",
            "phonemic_transcription",
            "phonetic_transcription",
            "gloss_line",
            "free_translation",
            "literal_translation",
            "notes",
            "source_type",
            "difficulty_level",
            "created_at",
            "updated_at",
            "words",
        ]
        read_only_fields = fields


class ExampleSentenceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleSentence
        fields = [
            "id",
            "language",
            "text_native",
            "text_romanized",
            "phonemic_transcription",
            "phonetic_transcription",
            "gloss_line",
            "free_translation",
            "literal_translation",
            "notes",
            "source_type",
            "difficulty_level",
        ]
        read_only_fields = ["id"]