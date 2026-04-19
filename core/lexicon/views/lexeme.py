from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from core.lexicon.models import Lexeme
from core.lexicon.serializers import LexemeReadSerializer, LexemeWriteSerializer
from core.common.permissions import CanEditProjectResource, CanDeleteProjectResource
from core.common.views import BaseModelViewSet


class LexemeViewSet(BaseModelViewSet):
    read_serializer_class = LexemeReadSerializer
    write_serializer_class = LexemeWriteSerializer
    permission_classes = [permissions.IsAuthenticated, CanEditProjectResource, CanDeleteProjectResource]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["lemma", "meaning_core"]
    ordering_fields = ["lemma", "created_at"]
    ordering = ["lemma"]

    def get_queryset(self):
        user = self.request.user
        qs = Lexeme.objects.select_related(
            "language",
            "language__project",
            "part_of_speech",
            "root_morpheme",
        ).prefetch_related(
            "senses",
            "forms",
            "outgoing_relations",
            "incoming_relations",
        )

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()