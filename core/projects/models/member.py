from django.db import models
from core.common.models.base import BaseModel


class ProjectMember(BaseModel):
    ROLE_CHOICES = [
        ("owner", "Owner"),
        ("admin", "Admin"),
        ("editor", "Editor"),
        ("viewer", "Viewer"),
    ]

    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="members"
    )
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="project_memberships"
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    can_edit = models.BooleanField(default=True)
    can_delete = models.BooleanField(default=False)
    can_invite = models.BooleanField(default=False)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("project", "user")
        ordering = ["project__name", "user__email"]

    def __str__(self):
        return f"{self.user.email} - {self.project.name}"