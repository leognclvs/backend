from rest_framework import serializers

from core.languages.models import Language
from core.projects.models import Project
from .metadata import LanguageMetadataSerializer
from .stage import LanguageStageSerializer
from .dialect import DialectSerializer


class LanguageReadSerializer(serializers.ModelSerializer):
    metadata = LanguageMetadataSerializer(read_only=True)
    stages = LanguageStageSerializer(many=True, read_only=True)
    dialects = DialectSerializer(many=True, read_only=True)
    created_by_email = serializers.EmailField(source="created_by.email", read_only=True)

    class Meta:
        model = Language
        fields = [
            "id",
            "project",
            "created_by",
            "created_by_email",
            "name",
            "native_name",
            "slug",
            "short_description",
            "full_description",
            "status",
            "visibility",
            "language_type",
            "inspiration_notes",
            "primary_word_order",
            "morphological_type",
            "alignment_type",
            "canonical_writing_direction",
            "version",
            "is_published",
            "created_at",
            "updated_at",
            "metadata",
            "stages",
            "dialects",
        ]
        read_only_fields = fields


class LanguageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = [
            "id",
            "project",
            "name",
            "native_name",
            "slug",
            "short_description",
            "full_description",
            "status",
            "visibility",
            "language_type",
            "inspiration_notes",
            "primary_word_order",
            "morphological_type",
            "alignment_type",
            "canonical_writing_direction",
            "version",
            "is_published",
        ]
        read_only_fields = ["id"]

    def validate_slug(self, value):
        value = value.strip().lower()
        qs = Language.objects.filter(slug=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError("Já existe um idioma com este slug.")

        return value

    def validate_project(self, value):
        request = self.context["request"]

        is_owner = value.owner_id == request.user.id
        is_member = value.members.filter(user=request.user).exists()

        if not (is_owner or is_member):
            raise serializers.ValidationError(
                "Você não tem permissão para usar este projeto."
            )

        return value

    def create(self, validated_data):
        request = self.context["request"]
        return Language.objects.create(created_by=request.user, **validated_data)