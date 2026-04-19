from django.db import models
from core.common.models.base import BaseModel


class PartOfSpeech(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="parts_of_speech"
    )
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    is_open_class = models.BooleanField(default=True)
    inflects = models.BooleanField(default=False)

    class Meta:
        unique_together = ("language", "code")
        ordering = ["name"]

    def __str__(self):
        return f"{self.language.name} - {self.name}"