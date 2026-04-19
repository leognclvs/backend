from rest_framework import serializers

from core.lexicon.models import Lexeme
from .sense import LexemeSenseSerializer
from .form import LexemeFormSerializer
from .relation import LexemeRelationSerializer


class LexemeReadSerializer(serializers.ModelSerializer):
    senses = LexemeSenseSerializer(many=True, read_only=True)
    forms = LexemeFormSerializer(many=True, read_only=True)
    outgoing_relations = LexemeRelationSerializer(many=True, read_only=True)
    incoming_relations = LexemeRelationSerializer(many=True, read_only=True)

    class Meta:
        model = Lexeme
        fields = [
            "id",
            "language",
            "lemma",
            "canonical_form",
            "romanized_form",
            "phonemic_form",
            "phonetic_form",
            "part_of_speech",
            "root_morpheme",
            "etymology_summary",
            "meaning_core",
            "usage_notes",
            "frequency_level",
            "register",
            "transitivity",
            "animacy_class",
            "classifier_type",
            "irregular",
            "is_published",
            "created_at",
            "updated_at",
            "senses",
            "forms",
            "outgoing_relations",
            "incoming_relations",
        ]
        read_only_fields = fields


class LexemeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lexeme
        fields = [
            "id",
            "language",
            "lemma",
            "canonical_form",
            "romanized_form",
            "phonemic_form",
            "phonetic_form",
            "part_of_speech",
            "root_morpheme",
            "etymology_summary",
            "meaning_core",
            "usage_notes",
            "frequency_level",
            "register",
            "transitivity",
            "animacy_class",
            "classifier_type",
            "irregular",
            "is_published",
        ]
        read_only_fields = ["id"]