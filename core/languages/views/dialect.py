from rest_framework import permissions

from core.languages.models import Dialect
from core.languages.serializers import DialectSerializer
from core.common.views import BaseModelViewSet


class DialectViewSet(BaseModelViewSet):
    queryset = Dialect.objects.select_related("language", "language__project")
    read_serializer_class = DialectSerializer
    write_serializer_class = DialectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()