from django.db import models
from core.common.models.base import BaseModel


class OrthographyRule(BaseModel):
    writing_system = models.ForeignKey(
        "writing.WritingSystem",
        on_delete=models.CASCADE,
        related_name="orthography_rules"
    )
    name = models.CharField(max_length=255)
    description = models.TextField()

    RULE_TYPE = [
        ("spelling", "Spelling"),
        ("phoneme_mapping", "Phoneme Mapping"),
        ("diacritic_usage", "Diacritic Usage"),
        ("exception", "Exception"),
    ]

    rule_type = models.CharField(max_length=50, choices=RULE_TYPE)
    priority = models.IntegerField(default=0)
    examples = models.TextField(blank=True)
    exceptions = models.TextField(blank=True)

    class Meta:
        ordering = ["priority", "name"]

    def __str__(self):
        return self.name