from rest_framework import permissions

from core.corpus.models import ExampleSentenceWord
from core.corpus.serializers import ExampleSentenceWordSerializer
from core.common.views import BaseModelViewSet


class ExampleSentenceWordViewSet(BaseModelViewSet):
    queryset = ExampleSentenceWord.objects.select_related(
        "example_sentence",
        "example_sentence__language",
        "lexeme",
    )
    read_serializer_class = ExampleSentenceWordSerializer
    write_serializer_class = ExampleSentenceWordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(example_sentence__language__project__members__user=user).distinct()