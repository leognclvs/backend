from rest_framework import serializers
from core.lexicon.models import Collocation, IdiomExpression


class CollocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collocation
        fields = [
            "id",
            "language",
            "expression",
            "meaning",
            "grammatical_pattern",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class IdiomExpressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdiomExpression
        fields = [
            "id",
            "language",
            "expression",
            "literal_meaning",
            "idiomatic_meaning",
            "usage_notes",
            "register",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]