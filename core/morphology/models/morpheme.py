from django.db import models
from core.common.models.base import BaseModel


class Morpheme(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="morphemes"
    )
    form = models.CharField(max_length=100)
    meaning = models.CharField(max_length=255)

    MORPHEME_TYPE = [
        ("root", "Root"),
        ("prefix", "Prefix"),
        ("suffix", "Suffix"),
        ("infix", "Infix"),
        ("circumfix", "Circumfix"),
    ]

    morpheme_type = models.CharField(max_length=20, choices=MORPHEME_TYPE)
    gloss = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["form"]

    def __str__(self):
        return self.form