from rest_framework import permissions

from core.lexicon.models import LexemeRelation
from core.lexicon.serializers import LexemeRelationSerializer
from core.common.views import BaseModelViewSet


class LexemeRelationViewSet(BaseModelViewSet):
    queryset = LexemeRelation.objects.select_related(
        "source_lexeme",
        "target_lexeme",
        "source_lexeme__language",
        "target_lexeme__language",
    )
    read_serializer_class = LexemeRelationSerializer
    write_serializer_class = LexemeRelationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(source_lexeme__language__project__members__user=user).distinct()