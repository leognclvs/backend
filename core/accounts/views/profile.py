from rest_framework import permissions

from core.accounts.models import Profile
from core.accounts.serializers import ProfileSerializer
from core.common.views import BaseModelViewSet


class ProfileViewSet(BaseModelViewSet):
    queryset = Profile.objects.all().select_related("user")
    read_serializer_class = ProfileSerializer
    write_serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return self.queryset
        return self.queryset.filter(user=user)