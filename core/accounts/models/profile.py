from django.db import models

from core.common.models.base import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="profile"
    )
    bio = models.TextField(blank=True)
    avatar = models.URLField(blank=True)
    preferred_language = models.CharField(max_length=50, blank=True)
    timezone = models.CharField(max_length=50, blank=True)
    public_visibility = models.BooleanField(default=True)
    website = models.URLField(blank=True)

    class Meta:
        ordering = ["user__email"]

    def __str__(self):
        return f"Profile - {self.user.email}"