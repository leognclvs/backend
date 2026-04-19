from django.db import models
from core.common.models.base import BaseModel


class ExampleSentence(BaseModel):
    SOURCE_TYPE_CHOICES = [
        ("manual", "Manual"),
        ("generated", "Generated"),
        ("corpus", "Corpus"),
    ]

    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="example_sentences"
    )
    text_native = models.TextField()
    text_romanized = models.TextField(blank=True)
    phonemic_transcription = models.TextField(blank=True)
    phonetic_transcription = models.TextField(blank=True)
    gloss_line = models.TextField(blank=True)
    free_translation = models.TextField(blank=True)
    literal_translation = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    source_type = models.CharField(max_length=20, choices=SOURCE_TYPE_CHOICES, default="manual")
    difficulty_level = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.text_native[:60]