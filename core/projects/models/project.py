from django.db import models
from core.common.models.base import BaseModel


class Project(BaseModel):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("active", "Active"),
        ("archived", "Archived"),
    ]

    VISIBILITY_CHOICES = [
        ("private", "Private"),
        ("public", "Public"),
    ]

    owner = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="owned_projects"
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    is_archived = models.BooleanField(default=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name