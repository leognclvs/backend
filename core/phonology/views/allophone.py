from rest_framework import permissions

from core.phonology.models import Allophone
from core.phonology.serializers import AllophoneSerializer
from core.common.views import BaseModelViewSet


class AllophoneViewSet(BaseModelViewSet):
    queryset = Allophone.objects.select_related("phoneme", "phoneme__language")
    read_serializer_class = AllophoneSerializer
    write_serializer_class = AllophoneSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(phoneme__language__project__members__user=user).distinct()