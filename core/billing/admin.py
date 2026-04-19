from django.contrib import admin
from .models import SubscriptionPlan, PlanFeature, UserSubscription

admin.site.register(SubscriptionPlan)
admin.site.register(PlanFeature)
admin.site.register(UserSubscription)