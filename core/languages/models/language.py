from django.db import models
from core.common.models.base import OwnedModel


class Language(OwnedModel):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("active", "Active"),
        ("deprecated", "Deprecated"),
        ("archived", "Archived"),
    ]

    VISIBILITY_CHOICES = [
        ("private", "Private"),
        ("public", "Public"),
    ]

    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="languages"
    )
    name = models.CharField(max_length=255)
    native_name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=255, blank=True)
    full_description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES)
    language_type = models.CharField(max_length=50, blank=True)
    inspiration_notes = models.TextField(blank=True)
    primary_word_order = models.CharField(max_length=10, blank=True)
    morphological_type = models.CharField(max_length=50, blank=True)
    alignment_type = models.CharField(max_length=50, blank=True)
    canonical_writing_direction = models.CharField(max_length=10, blank=True)
    version = models.CharField(max_length=20, default="1.0")
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name