from rest_framework import permissions

from core.phonology.models import PhonotacticRule
from core.phonology.serializers import PhonotacticRuleSerializer
from core.common.views import BaseModelViewSet


class PhonotacticRuleViewSet(BaseModelViewSet):
    queryset = PhonotacticRule.objects.select_related("language", "language__project")
    read_serializer_class = PhonotacticRuleSerializer
    write_serializer_class = PhonotacticRuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()