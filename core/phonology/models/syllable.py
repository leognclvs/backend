from django.db import models
from core.common.models.base import BaseModel


class SyllablePattern(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="syllable_patterns"
    )
    pattern = models.CharField(max_length=50)
    is_common = models.BooleanField(default=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("language", "pattern")
        ordering = ["pattern"]

    def __str__(self):
        return self.pattern