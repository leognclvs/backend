from rest_framework import permissions

from core.writing.models import ScriptSymbol
from core.writing.serializers import ScriptSymbolSerializer
from core.common.views import BaseModelViewSet


class ScriptSymbolViewSet(BaseModelViewSet):
    queryset = ScriptSymbol.objects.select_related("writing_system", "writing_system__language")
    read_serializer_class = ScriptSymbolSerializer
    write_serializer_class = ScriptSymbolSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(writing_system__language__project__members__user=user).distinct()