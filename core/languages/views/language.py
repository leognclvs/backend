from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from core.languages.models import Language
from core.languages.serializers import LanguageReadSerializer, LanguageWriteSerializer
from core.languages.filters import LanguageFilter
from core.common.permissions import CanEditProjectResource, CanDeleteProjectResource
from core.common.views import BaseModelViewSet


class LanguageViewSet(BaseModelViewSet):
    read_serializer_class = LanguageReadSerializer
    write_serializer_class = LanguageWriteSerializer
    permission_classes = [permissions.IsAuthenticated, CanEditProjectResource, CanDeleteProjectResource]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = LanguageFilter
    search_fields = ["name", "native_name", "short_description"]
    ordering_fields = ["created_at", "name"]
    ordering = ["-created_at"]

    def get_queryset(self):
        user = self.request.user
        qs = Language.objects.select_related(
            "project",
            "created_by",
            "metadata",
        ).prefetch_related(
            "stages",
            "dialects",
            "project__members",
        )

        if user.is_staff:
            return qs

        return qs.filter(project__members__user=user).distinct()