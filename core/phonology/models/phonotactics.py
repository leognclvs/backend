from django.db import models
from core.common.models.base import BaseModel


class PhonotacticRule(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="phonotactic_rules"
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    allowed_pattern = models.CharField(max_length=100)
    forbidden_pattern = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name