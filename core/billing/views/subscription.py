from decouple import config
from rest_framework import permissions, mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.billing.models import SubscriptionPlan, UserSubscription
from core.billing.serializers import SubscriptionPlanSerializer, UserSubscriptionSerializer


def build_payment_provider_config():
    provider = config("PAYMENT_PROVIDER", default="stripe").strip().lower()
    checkout_url_template = config("PAYMENT_CHECKOUT_URL_TEMPLATE", default="").strip()
    portal_url_template = config("PAYMENT_PORTAL_URL_TEMPLATE", default="").strip()
    publishable_key = config("PAYMENT_PUBLISHABLE_KEY", default="").strip()
    webhook_secret = config("PAYMENT_WEBHOOK_SECRET", default="").strip()

    return {
        "provider": provider or "stripe",
        "checkout_url_template": checkout_url_template,
        "portal_url_template": portal_url_template,
        "publishable_key_configured": bool(publishable_key),
        "webhook_secret_configured": bool(webhook_secret),
    }


class SubscriptionPlanViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    queryset = SubscriptionPlan.objects.prefetch_related("features").filter(
        is_active=True,
        is_public=True,
    )
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=["get"], permission_classes=[permissions.AllowAny])
    def payment_config(self, request):
        provider_config = build_payment_provider_config()
        return Response(
            {
                "provider": provider_config["provider"],
                "checkout_ready": bool(provider_config["checkout_url_template"]),
                "portal_ready": bool(provider_config["portal_url_template"]),
                "publishable_key_configured": provider_config["publishable_key_configured"],
                "webhook_secret_configured": provider_config["webhook_secret_configured"],
            }
        )

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def checkout(self, request, pk=None):
        plan = self.get_object()
        provider_config = build_payment_provider_config()
        checkout_template = provider_config["checkout_url_template"]

        checkout_url = ""
        if checkout_template and plan.provider_price_id:
            checkout_url = (
                checkout_template
                .replace("{PRICE_ID}", plan.provider_price_id)
                .replace("{PLAN_CODE}", plan.code)
                .replace("{USER_ID}", str(request.user.id))
                .replace("{EMAIL}", request.user.email)
            )

        return Response(
            {
                "provider": provider_config["provider"],
                "plan_code": plan.code,
                "plan_name": plan.name,
                "checkout_ready": bool(checkout_url),
                "checkout_url": checkout_url,
                "provider_price_id": plan.provider_price_id,
                "message": (
                    "Configuracao pronta para redirecionar ao provedor de pagamento."
                    if checkout_url
                    else "Plano sem configuracao completa de checkout no backend."
                ),
            },
            status=status.HTTP_200_OK,
        )


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

    @action(detail=False, methods=["post"])
    def portal(self, request):
        provider_config = build_payment_provider_config()
        portal_template = provider_config["portal_url_template"]
        latest_subscription = self.get_queryset().first()

        portal_url = ""
        if portal_template:
            subscription_id = (
                latest_subscription.external_subscription_id if latest_subscription else ""
            )
            portal_url = (
                portal_template
                .replace("{USER_ID}", str(request.user.id))
                .replace("{EMAIL}", request.user.email)
                .replace("{SUBSCRIPTION_ID}", subscription_id or "")
            )

        return Response(
            {
                "provider": provider_config["provider"],
                "portal_ready": bool(portal_url),
                "portal_url": portal_url,
                "message": (
                    "Portal do assinante pronto para uso."
                    if portal_url
                    else "Portal de billing ainda nao configurado no backend."
                ),
            },
            status=status.HTTP_200_OK,
        )
