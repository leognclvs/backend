from rest_framework import permissions

from core.lexicon.models import PartOfSpeech
from core.lexicon.serializers import PartOfSpeechSerializer
from core.common.views import BaseModelViewSet


class PartOfSpeechViewSet(BaseModelViewSet):
    queryset = PartOfSpeech.objects.select_related("language", "language__project")
    read_serializer_class = PartOfSpeechSerializer
    write_serializer_class = PartOfSpeechSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()