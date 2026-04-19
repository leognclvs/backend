from rest_framework import permissions

from core.languages.models import LanguageStage
from core.languages.serializers import LanguageStageSerializer
from core.common.views import BaseModelViewSet


class LanguageStageViewSet(BaseModelViewSet):
    queryset = LanguageStage.objects.select_related("language", "language__project")
    read_serializer_class = LanguageStageSerializer
    write_serializer_class = LanguageStageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()