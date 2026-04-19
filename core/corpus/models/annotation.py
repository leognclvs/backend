from django.db import models
from core.common.models.base import BaseModel


class CorpusAnnotation(BaseModel):
    corpus_text = models.ForeignKey(
        "corpus.CorpusText",
        on_delete=models.CASCADE,
        related_name="annotations"
    )
    token_index = models.PositiveIntegerField()
    token_text = models.CharField(max_length=255)
    lemma = models.CharField(max_length=255, blank=True)
    part_of_speech = models.CharField(max_length=100, blank=True)
    morphology = models.JSONField(default=dict, blank=True)
    syntax = models.JSONField(default=dict, blank=True)
    semantics = models.JSONField(default=dict, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["token_index"]

    def __str__(self):
        return f"{self.corpus_text.title} - {self.token_text}"