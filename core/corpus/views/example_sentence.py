from rest_framework import permissions

from core.corpus.models import ExampleSentence
from core.corpus.serializers import ExampleSentenceReadSerializer, ExampleSentenceWriteSerializer
from core.common.views import BaseModelViewSet


class ExampleSentenceViewSet(BaseModelViewSet):
    read_serializer_class = ExampleSentenceReadSerializer
    write_serializer_class = ExampleSentenceWriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = ExampleSentence.objects.select_related("language", "language__project").prefetch_related("words")

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()