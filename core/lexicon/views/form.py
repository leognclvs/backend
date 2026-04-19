from rest_framework import permissions

from core.lexicon.models import LexemeForm
from core.lexicon.serializers import LexemeFormSerializer
from core.common.views import BaseModelViewSet


class LexemeFormViewSet(BaseModelViewSet):
    queryset = LexemeForm.objects.select_related("lexeme", "lexeme__language")
    read_serializer_class = LexemeFormSerializer
    write_serializer_class = LexemeFormSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(lexeme__language__project__members__user=user).distinct()