from django.db import models
from core.common.models.base import BaseModel


class SoundChangeRule(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="sound_changes"
    )
    name = models.CharField(max_length=255)
    input_pattern = models.CharField(max_length=100)
    output_pattern = models.CharField(max_length=100)
    environment = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name