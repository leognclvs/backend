from django.db import models
from core.common.models.base import BaseModel


class Phoneme(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="phonemes"
    )
    ipa = models.CharField(max_length=50)

    PHONEME_TYPE = [
        ("vowel", "Vowel"),
        ("consonant", "Consonant"),
    ]

    phoneme_type = models.CharField(max_length=20, choices=PHONEME_TYPE)
    voicing = models.CharField(max_length=50, blank=True)
    place = models.CharField(max_length=50, blank=True)
    manner = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=50, blank=True)
    backness = models.CharField(max_length=50, blank=True)
    rounded = models.BooleanField(null=True, blank=True)
    nasal = models.BooleanField(default=False)
    length = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("language", "ipa")
        ordering = ["ipa"]

    def __str__(self):
        return self.ipa