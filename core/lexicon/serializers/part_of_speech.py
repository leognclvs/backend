from rest_framework import serializers
from core.lexicon.models import PartOfSpeech


class PartOfSpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartOfSpeech
        fields = [
            "id",
            "language",
            "name",
            "code",
            "description",
            "is_open_class",
            "inflects",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]