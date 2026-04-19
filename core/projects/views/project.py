from copy import deepcopy

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

from core.common.permissions import IsOwnerOrReadOnly
from core.common.views import BaseModelViewSet
from core.languages.models import Language
from core.lexicon.models import Lexeme
from core.phonology.models import Phoneme
from core.projects.models import Project, ProjectMember
from core.projects.serializers import ProjectReadSerializer, ProjectWriteSerializer


class ProjectViewSet(BaseModelViewSet):
    read_serializer_class = ProjectReadSerializer
    write_serializer_class = ProjectWriteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = "slug"

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name", "slug", "description"]
    ordering_fields = ["created_at", "updated_at", "name"]
    ordering = ["-updated_at"]

    def get_queryset(self):
        user = self.request.user
        qs = Project.objects.select_related("owner", "owner__profile").prefetch_related(
            "members",
            "members__user",
            "languages",
        )

        if user.is_staff:
            return qs

        return qs.filter(Q(owner=user) | Q(members__user=user)).distinct()

    @action(detail=True, methods=["post"])
    def archive(self, request, slug=None):
        project = self.get_object()
        project.is_archived = True
        project.status = "archived"
        project.save(update_fields=["is_archived", "status", "updated_at"])
        return Response(
            ProjectReadSerializer(project, context={"request": request}).data,
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["post"])
    def duplicate(self, request, slug=None):
        project = self.get_object()
        clone = deepcopy(project)
        clone.pk = None
        clone.id = None
        clone.name = f"{project.name} (Cópia)"

        base_slug = f"{project.slug}-copy"
        candidate = base_slug
        counter = 2
        while Project.objects.filter(slug=candidate).exists():
            candidate = f"{base_slug}-{counter}"
            counter += 1

        clone.slug = candidate
        clone.is_archived = False
        clone.status = "draft"
        clone.owner = request.user
        clone.save()

        ProjectMember.objects.get_or_create(
            project=clone,
            user=request.user,
            defaults={
                "role": "owner",
                "can_edit": True,
                "can_delete": True,
                "can_invite": True,
            },
        )

        return Response(
            ProjectReadSerializer(clone, context={"request": request}).data,
            status=status.HTTP_201_CREATED,
        )

    @action(detail=True, methods=["get"])
    def activity(self, request, slug=None):
        project = self.get_object()
        languages = Language.objects.filter(project=project).select_related("project").order_by("-updated_at")[:5]
        lexemes = Lexeme.objects.filter(language__project=project).select_related(
            "language",
            "language__project",
        ).order_by("-updated_at")[:5]
        phonemes = Phoneme.objects.filter(language__project=project).select_related(
            "language",
            "language__project",
        ).order_by("-updated_at")[:5]

        activity_items = [
            {
                "id": f"project-{project.id}",
                "entity_type": "project",
                "entity_id": str(project.id),
                "project_id": str(project.id),
                "language_id": None,
                "user_id": str(request.user.id),
                "user": {
                    "id": str(request.user.id),
                    "username": request.user.username,
                    "display_name": request.user.display_name or request.user.username,
                    "avatar_url": getattr(getattr(request.user, "profile", None), "avatar", ""),
                },
                "action": "archived" if project.is_archived else "updated",
                "created_at": project.updated_at,
                "description": f"Projeto {project.name} atualizado",
            }
        ]

        activity_items.extend(
            {
                "id": f"language-{language.id}",
                "entity_type": "language",
                "entity_id": str(language.id),
                "project_id": str(project.id),
                "language_id": str(language.id),
                "user_id": str(getattr(language.created_by, 'id', request.user.id)),
                "user": {
                    "id": str(getattr(language.created_by, "id", request.user.id)),
                    "username": getattr(language.created_by, "username", request.user.username),
                    "display_name": getattr(language.created_by, "display_name", "") or getattr(language.created_by, "username", request.user.username),
                    "avatar_url": getattr(getattr(getattr(language, "created_by", None), "profile", None), "avatar", ""),
                },
                "action": "published" if language.is_published else "updated",
                "created_at": language.updated_at,
                "description": f"Idioma {language.name} atualizado",
            }
            for language in languages
        )

        activity_items.extend(
            {
                "id": f"lexeme-{lexeme.id}",
                "entity_type": "lexeme",
                "entity_id": str(lexeme.id),
                "project_id": str(project.id),
                "language_id": str(lexeme.language_id),
                "user_id": str(request.user.id),
                "user": {
                    "id": str(request.user.id),
                    "username": request.user.username,
                    "display_name": request.user.display_name or request.user.username,
                    "avatar_url": getattr(getattr(request.user, "profile", None), "avatar", ""),
                },
                "action": "updated",
                "created_at": lexeme.updated_at,
                "description": f"Lexema {lexeme.lemma} atualizado",
            }
            for lexeme in lexemes
        )

        activity_items.extend(
            {
                "id": f"phoneme-{phoneme.id}",
                "entity_type": "phoneme",
                "entity_id": str(phoneme.id),
                "project_id": str(project.id),
                "language_id": str(phoneme.language_id),
                "user_id": str(request.user.id),
                "user": {
                    "id": str(request.user.id),
                    "username": request.user.username,
                    "display_name": request.user.display_name or request.user.username,
                    "avatar_url": getattr(getattr(request.user, "profile", None), "avatar", ""),
                },
                "action": "updated",
                "created_at": phoneme.updated_at,
                "description": f"Fonema {phoneme.ipa} atualizado",
            }
            for phoneme in phonemes
        )

        activity_items = sorted(
            activity_items,
            key=lambda item: item["created_at"],
            reverse=True,
        )

        page = self.paginate_queryset(activity_items)
        if page is not None:
            for item in page:
                item["created_at"] = item["created_at"].isoformat()
            return self.get_paginated_response(page)

        for item in activity_items:
            item["created_at"] = item["created_at"].isoformat()
        return Response(activity_items)
