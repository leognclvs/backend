from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Permite edição apenas ao owner do objeto.
    O objeto precisa ter atributo `owner`.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return getattr(obj, "owner_id", None) == request.user.id


class IsProjectOwner(BasePermission):
    """
    Permite acesso apenas ao owner do projeto relacionado.
    """

    def has_object_permission(self, request, view, obj):
        project = getattr(obj, "project", None)

        if project is None and hasattr(obj, "language"):
            project = getattr(obj.language, "project", None)

        if project is None:
            return False

        return project.owner_id == request.user.id


class IsProjectMember(BasePermission):
    """
    Permite acesso se o usuário for membro do projeto relacionado.
    """

    def has_object_permission(self, request, view, obj):
        project = getattr(obj, "project", None)

        if project is None and hasattr(obj, "language"):
            project = getattr(obj.language, "project", None)

        if project is None:
            return False

        return project.members.filter(user=request.user).exists()


class CanEditProjectResource(BasePermission):
    """
    Permite escrita para owner/admin ou membro com can_edit.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        project = getattr(obj, "project", None)

        if project is None and hasattr(obj, "language"):
            project = getattr(obj.language, "project", None)

        if project is None:
            return False

        membership = project.members.filter(user=request.user).first()
        if membership is None:
            return False

        return membership.role in ["owner", "admin"] or membership.can_edit


class CanDeleteProjectResource(BasePermission):
    """
    Permite delete apenas a owner/admin ou membro com can_delete.
    """

    def has_object_permission(self, request, view, obj):
        if request.method != "DELETE":
            return True

        project = getattr(obj, "project", None)

        if project is None and hasattr(obj, "language"):
            project = getattr(obj.language, "project", None)

        if project is None:
            return False

        membership = project.members.filter(user=request.user).first()
        if membership is None:
            return False

        return membership.role in ["owner", "admin"] or membership.can_delete


class CanInviteProjectMembers(BasePermission):
    """
    Permite gerenciar membros apenas a owner/admin ou quem tiver can_invite.
    """

    def has_object_permission(self, request, view, obj):
        project = getattr(obj, "project", None)
        if project is None:
            return False

        membership = project.members.filter(user=request.user).first()
        if membership is None:
            return False

        return membership.role in ["owner", "admin"] or membership.can_invite