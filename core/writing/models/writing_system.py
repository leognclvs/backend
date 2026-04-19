from django.db import models
from core.common.models.base import BaseModel


class WritingSystem(BaseModel):
    language = models.ForeignKey(
        "languages.Language",
        on_delete=models.CASCADE,
        related_name="writing_systems"
    )
    name = models.CharField(max_length=255)

    SYSTEM_TYPE = [
        ("alphabet", "Alphabet"),
        ("abjad", "Abjad"),
        ("abugida", "Abugida"),
        ("syllabary", "Syllabary"),
        ("logographic", "Logographic"),
        ("other", "Other"),
    ]

    type = models.CharField(max_length=20, choices=SYSTEM_TYPE)
    direction = models.CharField(max_length=10)
    writing_mode = models.CharField(max_length=20, blank=True)
    uses_spaces = models.BooleanField(default=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.language.name} - {self.name}"