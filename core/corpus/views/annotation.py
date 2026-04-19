from rest_framework import permissions

from core.corpus.models import CorpusAnnotation
from core.corpus.serializers import CorpusAnnotationSerializer
from core.common.views import BaseModelViewSet


class CorpusAnnotationViewSet(BaseModelViewSet):
    queryset = CorpusAnnotation.objects.select_related("corpus_text", "corpus_text__language")
    read_serializer_class = CorpusAnnotationSerializer
    write_serializer_class = CorpusAnnotationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(corpus_text__language__project__members__user=user).distinct()