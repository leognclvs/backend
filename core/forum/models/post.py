from django.conf import settings
from django.db import models

from core.common.models.base import BaseModel


class ForumPost(BaseModel):
    thread = models.ForeignKey(
        "forum.ForumThread",
        on_delete=models.CASCADE,
        related_name="posts",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="forum_posts",
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies",
    )
    content = models.TextField()
    is_solution = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.owner} @ {self.thread}"

