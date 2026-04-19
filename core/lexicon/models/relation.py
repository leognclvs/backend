from django.db import models
from core.common.models.base import BaseModel


class LexemeRelation(BaseModel):
    RELATION_TYPE_CHOICES = [
        ("synonym", "Synonym"),
        ("antonym", "Antonym"),
        ("hypernym", "Hypernym"),
        ("hyponym", "Hyponym"),
        ("meronym", "Meronym"),
        ("holonym", "Holonym"),
        ("derived_from", "Derived From"),
        ("cognate_of", "Cognate Of"),
        ("variant_of", "Variant Of"),
        ("related_to", "Related To"),
    ]

    source_lexeme = models.ForeignKey(
        "lexicon.Lexeme",
        on_delete=models.CASCADE,
        related_name="outgoing_relations"
    )
    target_lexeme = models.ForeignKey(
        "lexicon.Lexeme",
        on_delete=models.CASCADE,
        related_name="incoming_relations"
    )
    relation_type = models.CharField(max_length=30, choices=RELATION_TYPE_CHOICES)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["relation_type"]

    def __str__(self):
        return f"{self.source_lexeme} -> {self.relation_type} -> {self.target_lexeme}"