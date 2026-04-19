from rest_framework import permissions

from core.languages.models import LanguageMetadata
from core.languages.serializers import LanguageMetadataSerializer
from core.common.views import BaseModelViewSet


class LanguageMetadataViewSet(BaseModelViewSet):
    queryset = LanguageMetadata.objects.select_related("language", "language__project")
    read_serializer_class = LanguageMetadataSerializer
    write_serializer_class = LanguageMetadataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()