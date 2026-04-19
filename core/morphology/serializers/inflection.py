from rest_framework import serializers

from core.morphology.models import InflectionCategory, InflectionValue


class InflectionValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = InflectionValue
        fields = [
            "id",
            "category",
            "name",
            "abbreviation",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class InflectionCategoryReadSerializer(serializers.ModelSerializer):
    values = InflectionValueSerializer(many=True, read_only=True)

    class Meta:
        model = InflectionCategory
        fields = [
            "id",
            "language",
            "name",
            "description",
            "created_at",
            "updated_at",
            "values",
        ]
        read_only_fields = fields


class InflectionCategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InflectionCategory
        fields = [
            "id",
            "language",
            "name",
            "description",
        ]
        read_only_fields = ["id"]