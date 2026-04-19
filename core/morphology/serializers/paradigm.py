from rest_framework import serializers

from core.morphology.models import Paradigm, ParadigmCell


class ParadigmCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParadigmCell
        fields = [
            "id",
            "paradigm",
            "form",
            "grammatical_signature",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class ParadigmReadSerializer(serializers.ModelSerializer):
    cells = ParadigmCellSerializer(many=True, read_only=True)

    class Meta:
        model = Paradigm
        fields = [
            "id",
            "language",
            "name",
            "part_of_speech",
            "description",
            "created_at",
            "updated_at",
            "cells",
        ]
        read_only_fields = fields


class ParadigmWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields = [
            "id",
            "language",
            "name",
            "part_of_speech",
            "description",
        ]
        read_only_fields = ["id"]