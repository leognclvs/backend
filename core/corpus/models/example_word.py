from django.db import models
from core.common.models.base import BaseModel


class ExampleSentenceWord(BaseModel):
    example_sentence = models.ForeignKey(
        "corpus.ExampleSentence",
        on_delete=models.CASCADE,
        related_name="words"
    )
    position = models.PositiveIntegerField()
    surface_form = models.CharField(max_length=255)

    lexeme = models.ForeignKey(
        "lexicon.Lexeme",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="example_occurrences"
    )

    gloss = models.CharField(max_length=255, blank=True)
    grammatical_info = models.JSONField(default=dict, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("example_sentence", "position")
        ordering = ["position"]

    def __str__(self):
        return f"{self.example_sentence_id} - {self.surface_form}"