from django.db import models
from core.common.models.base import BaseModel


class LexemeSense(BaseModel):
    lexeme = models.ForeignKey(
        "lexicon.Lexeme",
        on_delete=models.CASCADE,
        related_name="senses"
    )
    sense_number = models.PositiveIntegerField(default=1)
    definition = models.TextField()
    semantic_domain = models.CharField(max_length=100, blank=True)
    connotation = models.CharField(max_length=50, blank=True)
    usage_context = models.TextField(blank=True)
    taboo_level = models.CharField(max_length=30, blank=True)
    figurative = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("lexeme", "sense_number")
        ordering = ["sense_number"]

    def __str__(self):
        return f"{self.lexeme.lemma} - sense {self.sense_number}"