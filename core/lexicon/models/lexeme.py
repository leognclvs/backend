from django.db import models
from core.common.models.base import BaseModel


class Lexeme(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="lexemes"
    )
    lemma = models.CharField(max_length=255)
    canonical_form = models.CharField(max_length=255, blank=True)
    romanized_form = models.CharField(max_length=255, blank=True)
    phonemic_form = models.CharField(max_length=255, blank=True)
    phonetic_form = models.CharField(max_length=255, blank=True)

    part_of_speech = models.ForeignKey(
        "lexicon.PartOfSpeech",
        on_delete=models.PROTECT,
        related_name="lexemes"
    )

    root_morpheme = models.ForeignKey(
        "morphology.Morpheme",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="lexemes"
    )

    etymology_summary = models.TextField(blank=True)
    meaning_core = models.CharField(max_length=255, blank=True)
    usage_notes = models.TextField(blank=True)
    frequency_level = models.CharField(max_length=50, blank=True)
    register = models.CharField(max_length=50, blank=True)
    transitivity = models.CharField(max_length=30, blank=True)
    animacy_class = models.CharField(max_length=50, blank=True)
    classifier_type = models.CharField(max_length=50, blank=True)
    irregular = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    class Meta:
        unique_together = ("language", "lemma", "part_of_speech")
        ordering = ["lemma"]

    def __str__(self):
        return self.lemma