from django.db import models
from core.common.models.base import BaseModel


class Collocation(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="collocations"
    )
    expression = models.CharField(max_length=255)
    meaning = models.TextField(blank=True)
    grammatical_pattern = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["expression"]

    def __str__(self):
        return self.expression


class IdiomExpression(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="idiom_expressions"
    )
    expression = models.CharField(max_length=255)
    literal_meaning = models.TextField(blank=True)
    idiomatic_meaning = models.TextField()
    usage_notes = models.TextField(blank=True)
    register = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["expression"]

    def __str__(self):
        return self.expression