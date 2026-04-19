from django.db import models
from core.common.models.base import BaseModel


class SubscriptionPlan(BaseModel):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    billing_cycle = models.CharField(max_length=20)
    trial_days = models.IntegerField(default=0)
    payment_provider = models.CharField(max_length=50, blank=True)
    provider_product_id = models.CharField(max_length=255, blank=True)
    provider_price_id = models.CharField(max_length=255, blank=True)
    cta_label = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    sort_order = models.IntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name
