from rest_framework import serializers
from core.corpus.models import CorpusAnnotation


class CorpusAnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorpusAnnotation
        fields = [
            "id",
            "corpus_text",
            "token_index",
            "token_text",
            "lemma",
            "part_of_speech",
            "morphology",
            "syntax",
            "semantics",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]