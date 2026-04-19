from rest_framework import permissions

from core.morphology.models import Morpheme
from core.morphology.serializers import MorphemeSerializer
from core.common.views import BaseModelViewSet


class MorphemeViewSet(BaseModelViewSet):
    queryset = Morpheme.objects.select_related("language", "language__project")
    read_serializer_class = MorphemeSerializer
    write_serializer_class = MorphemeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()