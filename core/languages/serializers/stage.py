from rest_framework import serializers
from core.languages.models import LanguageStage


class LanguageStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageStage
        fields = [
            "id",
            "name",
            "slug",
            "stage_order",
            "period_description",
            "description",
            "is_active_stage",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]