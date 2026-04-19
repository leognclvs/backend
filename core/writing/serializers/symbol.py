from rest_framework import serializers
from core.writing.models import ScriptSymbol


class ScriptSymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScriptSymbol
        fields = [
            "id",
            "writing_system",
            "symbol",
            "name",
            "symbol_type",
            "uppercase",
            "lowercase",
            "ipa_value",
            "romanization",
            "unicode_representation",
            "order",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]