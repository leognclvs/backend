from django.db import models
from core.common.models.base import BaseModel


class DerivationRule(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="derivation_rules"
    )
    name = models.CharField(max_length=255)
    source_category = models.CharField(max_length=50)
    target_category = models.CharField(max_length=50)
    transformation = models.CharField(max_length=255)
    semantic_effect = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name