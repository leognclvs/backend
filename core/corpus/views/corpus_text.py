from rest_framework import permissions

from core.corpus.models import CorpusText
from core.corpus.serializers import CorpusTextReadSerializer, CorpusTextWriteSerializer
from core.common.views import BaseModelViewSet


class CorpusTextViewSet(BaseModelViewSet):
    read_serializer_class = CorpusTextReadSerializer
    write_serializer_class = CorpusTextWriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = CorpusText.objects.select_related("language", "language__project").prefetch_related("annotations")

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()