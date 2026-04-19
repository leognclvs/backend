from rest_framework import permissions

from core.morphology.models import DerivationRule
from core.morphology.serializers import DerivationRuleSerializer
from core.common.views import BaseModelViewSet


class DerivationRuleViewSet(BaseModelViewSet):
    queryset = DerivationRule.objects.select_related("language", "language__project")
    read_serializer_class = DerivationRuleSerializer
    write_serializer_class = DerivationRuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()