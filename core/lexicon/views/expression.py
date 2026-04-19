from rest_framework import permissions

from core.lexicon.models import Collocation, IdiomExpression
from core.lexicon.serializers import CollocationSerializer, IdiomExpressionSerializer
from core.common.views import BaseModelViewSet


class CollocationViewSet(BaseModelViewSet):
    queryset = Collocation.objects.select_related("language", "language__project")
    read_serializer_class = CollocationSerializer
    write_serializer_class = CollocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()


class IdiomExpressionViewSet(BaseModelViewSet):
    queryset = IdiomExpression.objects.select_related("language", "language__project")
    read_serializer_class = IdiomExpressionSerializer
    write_serializer_class = IdiomExpressionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        qs = self.queryset

        if user.is_staff:
            return qs

        return qs.filter(language__project__members__user=user).distinct()