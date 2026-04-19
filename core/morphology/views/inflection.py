from rest_framework import permissions

from core.morphology.models import InflectionCategory, InflectionValue
from core.morphology.serializers import (
    InflectionCategoryReadSerializer,
    InflectionCategoryWriteSerializer,
    InflectionValueSerializer,
)
from core.common.views import BaseModelViewSet


class InflectionCategoryViewSet(BaseModelViewSet):
    read_serializer_class = InflectionCategoryReadSerializer
    write_serializer_class = InflectionCategoryWriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = InflectionCategory.objects.select_related("language", "language__project").prefetch_related("values")

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()


class InflectionValueViewSet(BaseModelViewSet):
    queryset = InflectionValue.objects.select_related("category", "category__language")
    read_serializer_class = InflectionValueSerializer
    write_serializer_class = InflectionValueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(category__language__project__members__user=user).distinct()