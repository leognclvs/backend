from django.conf import settings
from django.db import models

from core.common.models.base import BaseModel


class ForumThread(BaseModel):
    category = models.ForeignKey(
        "forum.ForumCategory",
        on_delete=models.PROTECT,
        related_name="threads",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="forum_threads",
    )
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=220, unique=True)
    content = models.TextField()
    is_pinned = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    last_activity_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-is_pinned", "-last_activity_at", "-updated_at"]

    def __str__(self):
        return self.title

