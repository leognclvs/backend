from rest_framework import serializers
from core.lexicon.models import LexemeRelation


class LexemeRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LexemeRelation
        fields = [
            "id",
            "source_lexeme",
            "target_lexeme",
            "relation_type",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate(self, attrs):
        source = attrs.get("source_lexeme")
        target = attrs.get("target_lexeme")

        if source == target:
            raise serializers.ValidationError(
                "Uma relação lexical não pode apontar para o mesmo lexema."
            )

        return attrs