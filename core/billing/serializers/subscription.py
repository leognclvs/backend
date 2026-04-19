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
            "is_active",
            "sort_order",
            "features",
            "created_at",
            "updated_at",
        ]
        read_only_fields = fields


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