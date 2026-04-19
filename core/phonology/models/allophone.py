from django.db import models
from core.common.models.base import BaseModel


class Allophone(BaseModel):
    phoneme = models.ForeignKey(
        "phonology.Phoneme",
        on_delete=models.CASCADE,
        related_name="allophones"
    )
    ipa = models.CharField(max_length=50)
    environment = models.TextField()
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["ipa"]

    def __str__(self):
        return self.ipa