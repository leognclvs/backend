from rest_framework import permissions

from core.lexicon.models import LexemeSense
from core.lexicon.serializers import LexemeSenseSerializer
from core.common.views import BaseModelViewSet


class LexemeSenseViewSet(BaseModelViewSet):
    queryset = LexemeSense.objects.select_related("lexeme", "lexeme__language")
    read_serializer_class = LexemeSenseSerializer
    write_serializer_class = LexemeSenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(lexeme__language__project__members__user=user).distinct()