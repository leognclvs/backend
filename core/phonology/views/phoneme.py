from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from core.phonology.models import Phoneme
from core.phonology.serializers import PhonemeReadSerializer, PhonemeWriteSerializer
from core.common.permissions import CanEditProjectResource, CanDeleteProjectResource
from core.common.views import BaseModelViewSet


class PhonemeViewSet(BaseModelViewSet):
    read_serializer_class = PhonemeReadSerializer
    write_serializer_class = PhonemeWriteSerializer
    permission_classes = [permissions.IsAuthenticated, CanEditProjectResource, CanDeleteProjectResource]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["ipa"]
    ordering_fields = ["created_at", "ipa"]
    ordering = ["ipa"]

    def get_queryset(self):
        user = self.request.user
        qs = Phoneme.objects.select_related("language", "language__project").prefetch_related("allophones")

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()