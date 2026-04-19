from django.db import models
from core.common.models.base import BaseModel


class ScriptSymbol(BaseModel):
    writing_system = models.ForeignKey(
        "writing.WritingSystem",
        on_delete=models.CASCADE,
        related_name="symbols"
    )
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    SYMBOL_TYPE = [
        ("letter", "Letter"),
        ("diacritic", "Diacritic"),
        ("digit", "Digit"),
        ("punctuation", "Punctuation"),
        ("other", "Other"),
    ]

    symbol_type = models.CharField(max_length=20, choices=SYMBOL_TYPE)
    uppercase = models.CharField(max_length=10, blank=True)
    lowercase = models.CharField(max_length=10, blank=True)
    ipa_value = models.CharField(max_length=50, blank=True)
    romanization = models.CharField(max_length=50, blank=True)
    unicode_representation = models.CharField(max_length=50, blank=True)
    order = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ("writing_system", "symbol")
        ordering = ["order", "symbol"]

    def __str__(self):
        return self.symbol