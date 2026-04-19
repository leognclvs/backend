from rest_framework import serializers

from core.phonology.models import Phoneme
from .allophone import AllophoneSerializer


class PhonemeReadSerializer(serializers.ModelSerializer):
    allophones = AllophoneSerializer(many=True, read_only=True)

    class Meta:
        model = Phoneme
        fields = [
            "id",
            "language",
            "ipa",
            "phoneme_type",
            "voicing",
            "place",
            "manner",
            "height",
            "backness",
            "rounded",
            "nasal",
            "length",
            "notes",
            "created_at",
            "updated_at",
            "allophones",
        ]
        read_only_fields = fields


class PhonemeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phoneme
        fields = [
            "id",
            "language",
            "ipa",
            "phoneme_type",
            "voicing",
            "place",
            "manner",
            "height",
            "backness",
            "rounded",
            "nasal",
            "length",
            "notes",
        ]
        read_only_fields = ["id"]