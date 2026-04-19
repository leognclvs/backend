from rest_framework import serializers

from core.corpus.models import CorpusText
from .annotation import CorpusAnnotationSerializer


class CorpusTextReadSerializer(serializers.ModelSerializer):
    annotations = CorpusAnnotationSerializer(many=True, read_only=True)

    class Meta:
        model = CorpusText
        fields = [
            "id",
            "language",
            "title",
            "text_type",
            "content",
            "translation",
            "annotation_level",
            "notes",
            "created_at",
            "updated_at",
            "annotations",
        ]
        read_only_fields = fields


class CorpusTextWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorpusText
        fields = [
            "id",
            "language",
            "title",
            "text_type",
            "content",
            "translation",
            "annotation_level",
            "notes",
        ]
        read_only_fields = ["id"]