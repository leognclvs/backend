from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.accounts.models import User
from core.projects.models import Project


class ProjectAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="leo@example.com",
            username="leo",
            password="SenhaForte123!"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_project(self):
        url = reverse("project-list")
        payload = {
            "name": "Meu Projeto",
            "slug": "meu-projeto",
            "description": "Projeto de idioma",
            "visibility": "private",
            "status": "active",
            "is_archived": False
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.first().owner, self.user)