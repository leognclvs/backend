from rest_framework import permissions

from core.morphology.models import Paradigm, ParadigmCell
from core.morphology.serializers import (
    ParadigmReadSerializer,
    ParadigmWriteSerializer,
    ParadigmCellSerializer,
)
from core.common.views import BaseModelViewSet


class ParadigmViewSet(BaseModelViewSet):
    read_serializer_class = ParadigmReadSerializer
    write_serializer_class = ParadigmWriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = Paradigm.objects.select_related("language", "language__project").prefetch_related("cells")

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()


class ParadigmCellViewSet(BaseModelViewSet):
    queryset = ParadigmCell.objects.select_related("paradigm", "paradigm__language")
    read_serializer_class = ParadigmCellSerializer
    write_serializer_class = ParadigmCellSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(paradigm__language__project__members__user=user).distinct()