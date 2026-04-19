from rest_framework import serializers
from core.morphology.models import Morpheme


class MorphemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morpheme
        fields = [
            "id",
            "language",
            "form",
            "meaning",
            "morpheme_type",
            "gloss",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]