from django.db.models import Count, Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.languages.models import Language
from core.lexicon.models import Lexeme
from core.phonology.models import Phoneme
from core.projects.models import Project


class DashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user

        projects = (
            Project.objects.filter(Q(owner=user) | Q(members__user=user))
            .select_related("owner")
            .prefetch_related("languages")
            .distinct()
        )

        languages = Language.objects.filter(project__in=projects).select_related("project")
        lexemes = Lexeme.objects.filter(language__in=languages).select_related("language", "language__project")
        phonemes = Phoneme.objects.filter(language__in=languages).select_related("language", "language__project")

        recent_languages = (
            languages.annotate(lexeme_total=Count("lexemes"))
            .order_by("-updated_at")[:5]
        )

        recent_activity = []

        for project in projects.order_by("-updated_at")[:3]:
            recent_activity.append(
                {
                    "id": f"project-{project.id}",
                    "action": f"Projeto {project.name} atualizado",
                    "language": project.name,
                    "time": project.updated_at.strftime("%d/%m/%Y %H:%M"),
                    "href": f"/projetos/{project.slug}",
                    "created_at": project.updated_at,
                }
            )

        for language in languages.order_by("-updated_at")[:4]:
            recent_activity.append(
                {
                    "id": f"language-{language.id}",
                    "action": f"Idioma {language.name} atualizado",
                    "language": language.project.name,
                    "time": language.updated_at.strftime("%d/%m/%Y %H:%M"),
                    "href": f"/projetos/{language.project.slug}/idiomas/{language.slug}",
                    "created_at": language.updated_at,
                }
            )

        for lexeme in lexemes.order_by("-updated_at")[:4]:
            recent_activity.append(
                {
                    "id": f"lexeme-{lexeme.id}",
                    "action": f"Lexema {lexeme.lemma} atualizado",
                    "language": lexeme.language.name,
                    "time": lexeme.updated_at.strftime("%d/%m/%Y %H:%M"),
                    "href": f"/projetos/{lexeme.language.project.slug}/idiomas/{lexeme.language.slug}",
                    "created_at": lexeme.updated_at,
                }
            )

        recent_activity = sorted(
            recent_activity,
            key=lambda item: item["created_at"],
            reverse=True,
        )[:8]

        for item in recent_activity:
            item.pop("created_at", None)

        return Response(
            {
                "metrics": {
                    "projects": projects.count(),
                    "languages": languages.count(),
                    "lexemes": lexemes.count(),
                    "phonemes": phonemes.count(),
                },
                "recent_languages": [
                    {
                        "id": str(language.id),
                        "name": language.name,
                        "project": language.project.name,
                        "project_slug": language.project.slug,
                        "slug": language.slug,
                        "count": language.lexeme_total,
                        "module": "Léxico",
                    }
                    for language in recent_languages
                ],
                "recent_activity": recent_activity,
            }
        )
