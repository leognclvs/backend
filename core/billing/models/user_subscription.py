from django.db import models
from core.common.models.base import BaseModel


class UserSubscription(BaseModel):
    STATUS_CHOICES = [
        ("trial", "Trial"),
        ("active", "Active"),
        ("past_due", "Past Due"),
        ("canceled", "Canceled"),
        ("expired", "Expired"),
    ]

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="subscriptions"
    )
    plan = models.ForeignKey(
        "billing.SubscriptionPlan",
        on_delete=models.PROTECT,
        related_name="subscriptions"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    started_at = models.DateTimeField()
    expires_at = models.DateTimeField(null=True, blank=True)
    renewal_type = models.CharField(max_length=20)
    external_customer_id = models.CharField(max_length=255, blank=True)
    external_subscription_id = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["-started_at"]

    def __str__(self):
        return f"{self.user.email} - {self.plan.name}"