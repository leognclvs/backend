from rest_framework import permissions, mixins, viewsets

from core.billing.models import SubscriptionPlan, UserSubscription
from core.billing.serializers import SubscriptionPlanSerializer, UserSubscriptionSerializer


class SubscriptionPlanViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    queryset = SubscriptionPlan.objects.prefetch_related("features").filter(is_active=True)
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [permissions.AllowAny]


class UserSubscriptionViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    serializer_class = UserSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = UserSubscription.objects.select_related("plan").prefetch_related("plan__features")
        user = self.request.user
        if user.is_staff:
            return qs
        return qs.filter(user=user)