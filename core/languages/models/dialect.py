from django.db import models
from core.common.models.base import BaseModel


class Dialect(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="dialects"
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    region = models.CharField(max_length=255, blank=True)
    social_group = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    mutual_intelligibility_notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("language", "slug")
        ordering = ["name"]

    def __str__(self):
        return f"{self.language.name} - {self.name}"