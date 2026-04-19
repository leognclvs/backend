from django.db import models
from core.common.models.base import BaseModel


class Translation(BaseModel):
    TRANSLATION_TYPE_CHOICES = [
        ("literal", "Literal"),
        ("free", "Free"),
        ("adapted", "Adapted"),
        ("scholarly", "Scholarly"),
    ]

    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="translations"
    )
    source_text = models.TextField()
    target_text = models.TextField()
    source_language_name = models.CharField(max_length=100)
    target_language_name = models.CharField(max_length=100)
    translation_type = models.CharField(max_length=20, choices=TRANSLATION_TYPE_CHOICES, default="free")
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["source_language_name", "target_language_name"]

    def __str__(self):
        return f"{self.source_language_name} -> {self.target_language_name}"