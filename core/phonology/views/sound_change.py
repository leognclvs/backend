from rest_framework import permissions

from core.phonology.models import SoundChangeRule
from core.phonology.serializers import SoundChangeRuleSerializer
from core.common.views import BaseModelViewSet


class SoundChangeRuleViewSet(BaseModelViewSet):
    queryset = SoundChangeRule.objects.select_related("language", "language__project")
    read_serializer_class = SoundChangeRuleSerializer
    write_serializer_class = SoundChangeRuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()