from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle

from core.accounts.models import User
from core.accounts.serializers import UserSerializer, UserCreateSerializer
from core.common.views import BaseModelViewSet


class UserViewSet(BaseModelViewSet):
    queryset = User.objects.all().select_related("profile")
    read_serializer_class = UserCreateSerializer
    write_serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    permission_classes_by_action = {
        "create": [permissions.AllowAny],
        "me": [permissions.IsAuthenticated],
    }

    def get_throttles(self):
        if self.action == "create":
            throttle = ScopedRateThrottle()
            throttle.scope = "register"
            return [throttle]
        return super().get_throttles()

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return self.queryset
        return self.queryset.filter(pk=user.pk)

    @action(detail=False, methods=["get"])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)