from rest_framework import serializers

from core.billing.models import SubscriptionPlan, PlanFeature, UserSubscription


class PlanFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanFeature
        fields = [
            "id",
            "feature_code",
            "feature_name",
            "limit_value",
            "is_enabled",
            "notes",
        ]
        read_only_fields = fields


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    features = PlanFeatureSerializer(many=True, read_only=True)
    checkout_ready = serializers.SerializerMethodField()

    class Meta:
        model = SubscriptionPlan
        fields = [
            "id",
            "code",
            "name",
            "description",
            "price",
            "currency",
            "billing_cycle",
            "trial_days",
            "payment_provider",
            "cta_label",
            "is_active",
            "is_public",
            "sort_order",
            "checkout_ready",
            "features",
            "created_at",
            "updated_at",
        ]
        read_only_fields = fields

    def get_checkout_ready(self, obj):
        return bool(obj.payment_provider and obj.provider_price_id)


class UserSubscriptionSerializer(serializers.ModelSerializer):
    plan = SubscriptionPlanSerializer(read_only=True)

    class Meta:
        model = UserSubscription
        fields = [
            "id",
            "plan",
            "status",
            "started_at",
            "expires_at",
            "renewal_type",
            "external_customer_id",
            "external_subscription_id",
            "created_at",
            "updated_at",
        ]
        read_only_fields = fields
