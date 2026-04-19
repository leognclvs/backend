from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from core.projects.models import Project
from core.projects.serializers import ProjectReadSerializer, ProjectWriteSerializer
from core.common.permissions import IsOwnerOrReadOnly
from core.common.views import BaseModelViewSet


class ProjectViewSet(BaseModelViewSet):
    read_serializer_class = ProjectReadSerializer
    write_serializer_class = ProjectWriteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name", "slug"]
    ordering_fields = ["created_at", "name"]
    ordering = ["-created_at"]

    def get_queryset(self):
        user = self.request.user
        qs = Project.objects.select_related("owner").prefetch_related("members", "members__user")

        if user.is_staff:
            return qs

        return qs.filter(members__user=user).distinct()