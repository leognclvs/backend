from rest_framework import serializers

from core.writing.models import WritingSystem
from .symbol import ScriptSymbolSerializer
from .orthography import OrthographyRuleSerializer


class WritingSystemReadSerializer(serializers.ModelSerializer):
    symbols = ScriptSymbolSerializer(many=True, read_only=True)
    orthography_rules = OrthographyRuleSerializer(many=True, read_only=True)

    class Meta:
        model = WritingSystem
        fields = [
            "id",
            "language",
            "name",
            "type",
            "direction",
            "writing_mode",
            "uses_spaces",
            "notes",
            "created_at",
            "updated_at",
            "symbols",
            "orthography_rules",
        ]
        read_only_fields = fields


class WritingSystemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = WritingSystem
        fields = [
            "id",
            "language",
            "name",
            "type",
            "direction",
            "writing_mode",
            "uses_spaces",
            "notes",
        ]
        read_only_fields = ["id"]