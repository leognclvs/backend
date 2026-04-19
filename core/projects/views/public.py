from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from core.projects.models import Project
from core.projects.serializers import ProjectReadSerializer

class PublicProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Renders all projects that have visibility set to 'public'.
    """
    serializer_class = ProjectReadSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "name", "updated_at"]
    ordering = ["-updated_at"]

    def get_queryset(self):
        qs = Project.objects.select_related(
            "owner",
        ).filter(visibility="public")
        
        return qs
