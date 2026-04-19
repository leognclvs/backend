from django.db import models
from core.common.models.base import BaseModel


class InflectionCategory(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="inflection_categories"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ("language", "name")
        ordering = ["name"]

    def __str__(self):
        return self.name


class InflectionValue(BaseModel):
    category = models.ForeignKey(
        "morphology.InflectionCategory",
        on_delete=models.CASCADE,
        related_name="values"
    )
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ("category", "name")
        ordering = ["name"]

    def __str__(self):
        return self.name