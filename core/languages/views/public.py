from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from core.languages.models import Language
from core.languages.serializers import LanguageReadSerializer

class PublicLanguageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Renders all languages that have visibility set to 'public'.
    """
    serializer_class = LanguageReadSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name", "native_name", "short_description"]
    ordering_fields = ["created_at", "name", "updated_at"]
    ordering = ["-updated_at"]

    def get_queryset(self):
        qs = Language.objects.select_related(
            "project",
            "created_by",
            "metadata",
        ).filter(visibility="public")
        
        return qs
