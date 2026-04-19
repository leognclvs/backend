from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.accounts.models import User
from core.projects.models import Project, ProjectMember
from core.languages.models import Language


class ProjectPermissionAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_user(
            email="owner@example.com",
            username="owner",
            password="SenhaForte123!",
        )
        self.viewer = User.objects.create_user(
            email="viewer@example.com",
            username="viewer",
            password="SenhaForte123!",
        )

        self.project = Project.objects.create(
            owner=self.owner,
            name="Projeto Seguro",
            slug="projeto-seguro",
            description="desc",
            visibility="private",
            status="active",
            is_archived=False,
        )

        ProjectMember.objects.create(
            project=self.project,
            user=self.owner,
            role="owner",
            can_edit=True,
            can_delete=True,
            can_invite=True,
        )

        ProjectMember.objects.create(
            project=self.project,
            user=self.viewer,
            role="viewer",
            can_edit=False,
            can_delete=False,
            can_invite=False,
        )

        self.language = Language.objects.create(
            project=self.project,
            created_by=self.owner,
            name="Idioma Seguro",
            native_name="Idioma Seguro",
            slug="idioma-seguro",
            short_description="desc",
            full_description="desc",
            status="active",
            visibility="private",
            language_type="constructed",
            inspiration_notes="",
            primary_word_order="SOV",
            morphological_type="agglutinative",
            alignment_type="nominative-accusative",
            canonical_writing_direction="LTR",
            version="1.0",
            is_published=False,
        )

    def test_viewer_cannot_patch_language(self):
        self.client.force_authenticate(user=self.viewer)
        url = reverse("language-detail", args=[self.language.id])

        response = self.client.patch(
            url,
            {"short_description": "alterado"},
            format="json",
        )

        self.assertIn(response.status_code, [status.HTTP_403_FORBIDDEN, status.HTTP_404_NOT_FOUND])