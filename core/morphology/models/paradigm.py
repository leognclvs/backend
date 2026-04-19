from django.db import models
from core.common.models.base import BaseModel


class Paradigm(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="paradigms"
    )
    name = models.CharField(max_length=100)
    part_of_speech = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class ParadigmCell(BaseModel):
    paradigm = models.ForeignKey(
        "morphology.Paradigm",
        on_delete=models.CASCADE,
        related_name="cells"
    )
    form = models.CharField(max_length=100)
    grammatical_signature = models.JSONField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["form"]

    def __str__(self):
        return self.form