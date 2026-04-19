from rest_framework import serializers
from core.writing.models import OrthographyRule


class OrthographyRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrthographyRule
        fields = [
            "id",
            "writing_system",
            "name",
            "description",
            "rule_type",
            "priority",
            "examples",
            "exceptions",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]