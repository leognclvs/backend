from django.db import models
from core.common.models.base import BaseModel


class CorpusText(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="corpus_texts"
    )
    title = models.CharField(max_length=255)
    text_type = models.CharField(max_length=50, blank=True)
    content = models.TextField()
    translation = models.TextField(blank=True)
    annotation_level = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title