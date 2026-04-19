from rest_framework import serializers
from core.languages.models import Dialect


class DialectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dialect
        fields = [
            "id",
            "name",
            "slug",
            "region",
            "social_group",
            "description",
            "mutual_intelligibility_notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]