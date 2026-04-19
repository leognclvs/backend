from rest_framework import permissions

from core.writing.models import WritingSystem
from core.writing.serializers import WritingSystemReadSerializer, WritingSystemWriteSerializer
from core.common.views import BaseModelViewSet


class WritingSystemViewSet(BaseModelViewSet):
    read_serializer_class = WritingSystemReadSerializer
    write_serializer_class = WritingSystemWriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = WritingSystem.objects.select_related("language", "language__project").prefetch_related(
            "symbols",
            "orthography_rules",
        )

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()