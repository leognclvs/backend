from rest_framework import permissions

from core.phonology.models import SyllablePattern
from core.phonology.serializers import SyllablePatternSerializer
from core.common.views import BaseModelViewSet


class SyllablePatternViewSet(BaseModelViewSet):
    queryset = SyllablePattern.objects.select_related("language", "language__project")
    read_serializer_class = SyllablePatternSerializer
    write_serializer_class = SyllablePatternSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()