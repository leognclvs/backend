from rest_framework import serializers
from core.morphology.models import DerivationRule


class DerivationRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DerivationRule
        fields = [
            "id",
            "language",
            "name",
            "source_category",
            "target_category",
            "transformation",
            "semantic_effect",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]