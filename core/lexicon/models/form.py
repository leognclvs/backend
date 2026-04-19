from django.db import models
from core.common.models.base import BaseModel


class LexemeForm(BaseModel):
    FORM_TYPE_CHOICES = [
        ("base", "Base"),
        ("inflected", "Inflected"),
        ("derived", "Derived"),
        ("variant", "Variant"),
    ]

    lexeme = models.ForeignKey(
        "lexicon.Lexeme",
        on_delete=models.CASCADE,
        related_name="forms"
    )
    form = models.CharField(max_length=255)
    form_type = models.CharField(max_length=20, choices=FORM_TYPE_CHOICES, default="base")
    phonological_form = models.CharField(max_length=255, blank=True)
    orthographic_form = models.CharField(max_length=255, blank=True)
    grammatical_signature = models.JSONField(default=dict, blank=True)
    is_irregular = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["form"]

    def __str__(self):
        return self.form