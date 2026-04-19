from django.db import models
from core.common.models.base import BaseModel


class LanguageMetadata(BaseModel):
    language = models.OneToOneField(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="metadata"
    )
    fictional_region = models.CharField(max_length=255, blank=True)
    real_world_influences = models.TextField(blank=True)
    cultural_notes = models.TextField(blank=True)
    historical_notes = models.TextField(blank=True)
    phonological_notes = models.TextField(blank=True)
    grammatical_notes = models.TextField(blank=True)
    estimated_speakers = models.IntegerField(null=True, blank=True)
    difficulty_level = models.CharField(max_length=50, blank=True)
    tags = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"Metadata - {self.language.name}"