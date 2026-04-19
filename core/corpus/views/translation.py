from rest_framework import permissions

from core.corpus.models import Translation
from core.corpus.serializers import TranslationSerializer
from core.common.views import BaseModelViewSet


class TranslationViewSet(BaseModelViewSet):
    queryset = Translation.objects.select_related("language", "language__project")
    read_serializer_class = TranslationSerializer
    write_serializer_class = TranslationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()