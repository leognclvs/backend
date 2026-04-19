from rest_framework import permissions

from core.writing.models import OrthographyRule
from core.writing.serializers import OrthographyRuleSerializer
from core.common.views import BaseModelViewSet


class OrthographyRuleViewSet(BaseModelViewSet):
    queryset = OrthographyRule.objects.select_related("writing_system", "writing_system__language")
    read_serializer_class = OrthographyRuleSerializer
    write_serializer_class = OrthographyRuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(writing_system__language__project__members__user=user).distinct()