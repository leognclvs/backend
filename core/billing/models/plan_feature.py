from django.db import models
from core.common.models.base import BaseModel


class PlanFeature(BaseModel):
    plan = models.ForeignKey(
        "billing.SubscriptionPlan",
        on_delete=models.CASCADE,
        related_name="features"
    )
    feature_code = models.CharField(max_length=100)
    feature_name = models.CharField(max_length=100)
    limit_value = models.IntegerField(null=True, blank=True)
    is_enabled = models.BooleanField(default=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("plan", "feature_code")
        ordering = ["feature_code"]

    def __str__(self):
        return f"{self.plan.name} - {self.feature_code}"