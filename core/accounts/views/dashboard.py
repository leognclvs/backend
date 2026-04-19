from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.projects.models import Project
from core.languages.models import Language
from core.lexicon.models import Lexeme
from core.phonology.models import Phoneme

class DashboardSummaryView(APIView):
    """
    Returns overarching statistics for the currently authenticated user.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user

        # Get user's projects
        projects = Project.objects.filter(owner=user)
        project_count = projects.count()

        # Get languages across all user's projects
        languages = Language.objects.filter(project__owner=user)
        language_count = languages.count()

        # Get lexemes and phonemes from those languages
        lexeme_count = Lexeme.objects.filter(language__in=languages).count()
        phoneme_count = Phoneme.objects.filter(language__in=languages).count()

        # Recent languages (limit to 5)
        recent_langs = languages.order_by('-updated_at')[:5]
        recent_languages_data = [
            {
                "id": str(lang.id),
                "name": lang.name,
                "project": lang.project.name,
                "count": Lexeme.objects.filter(language=lang).count(), # Example: lexeme count
                "module": "Idioma"
            }
            for lang in recent_langs
        ]

        # Activity could be mocked or queried if an Activity model exists
        # For now, return a basic list of 0.
        recent_activity = []

        return Response({
            "metrics": {
                "projects": project_count,
                "languages": language_count,
                "lexemes": lexeme_count,
                "phonemes": phoneme_count,
            },
            "recent_languages": recent_languages_data,
            "recent_activity": recent_activity
        })
