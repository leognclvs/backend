from rest_framework import serializers
from core.phonology.models import PhonotacticRule


class PhonotacticRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhonotacticRule
        fields = [
            "id",
            "language",
            "name",
            "description",
            "allowed_pattern",
            "forbidden_pattern",
            "position",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]