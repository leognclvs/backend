from rest_framework import viewsets


class ReadWriteSerializerMixin:
    read_serializer_class = None
    write_serializer_class = None

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            if self.read_serializer_class is None:
                raise AssertionError("read_serializer_class não definido.")
            return self.read_serializer_class

        if self.write_serializer_class is None:
            raise AssertionError("write_serializer_class não definido.")
        return self.write_serializer_class


class ActionPermissionMixin:
    permission_classes_by_action = {}

    def get_permissions(self):
        try:
            permission_classes = self.permission_classes_by_action[self.action]
        except KeyError:
            permission_classes = self.permission_classes

        return [permission() for permission in permission_classes]


class BaseModelViewSet(ReadWriteSerializerMixin, ActionPermissionMixin, viewsets.ModelViewSet):
    pass