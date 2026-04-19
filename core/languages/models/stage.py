from django.db import models
from core.common.models.base import BaseModel


class LanguageStage(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="stages"
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    stage_order = models.IntegerField()
    period_description = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    is_active_stage = models.BooleanField(default=False)

    class Meta:
        unique_together = ("language", "slug")
        ordering = ["stage_order"]

    def __str__(self):
        return f"{self.language.name} - {self.name}"