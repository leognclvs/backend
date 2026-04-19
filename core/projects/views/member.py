from rest_framework import permissions

from core.projects.models import ProjectMember
from core.projects.serializers import ProjectMemberSerializer
from core.common.permissions import CanInviteProjectMembers, CanDeleteProjectResource
from core.common.views import BaseModelViewSet


class ProjectMemberViewSet(BaseModelViewSet):
    queryset = ProjectMember.objects.select_related("project", "user")
    read_serializer_class = ProjectMemberSerializer
    write_serializer_class = ProjectMemberSerializer
    permission_classes = [permissions.IsAuthenticated, CanInviteProjectMembers, CanDeleteProjectResource]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(project__members__user=user).distinct()