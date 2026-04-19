from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.accounts.models import User
from core.projects.models import Project, ProjectMember
from core.languages.models import Language


class LanguageAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="leo@example.com",
            username="leo",
            password="SenhaForte123!"
        )
        self.project = Project.objects.create(
            owner=self.user,
            name="Projeto A",
            slug="projeto-a",
            description="desc",
            visibility="private",
            status="active",
            is_archived=False
        )
        ProjectMember.objects.create(
            project=self.project,
            user=self.user,
            role="owner",
            can_edit=True,
            can_delete=True,
            can_invite=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_create_language(self):
        url = reverse("language-list")
        payload = {
            "project": str(self.project.id),
            "name": "Lingua X",
            "native_name": "Lingua X",
            "slug": "lingua-x",
            "short_description": "Teste",
            "full_description": "Idioma de teste",
            "status": "active",
            "visibility": "private",
            "language_type": "constructed",
            "inspiration_notes": "",
            "primary_word_order": "SOV",
            "morphological_type": "agglutinative",
            "alignment_type": "nominative-accusative",
            "canonical_writing_direction": "LTR",
            "version": "1.0",
            "is_published": False
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Language.objects.count(), 1)