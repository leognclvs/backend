from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.accounts.models import User


class AuthTokenAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="leo@example.com",
            username="leo",
            password="SenhaForte123!",
        )

    def test_obtain_jwt_token(self):
        url = reverse("token_obtain_pair")
        payload = {
            "email": "leo@example.com",
            "password": "SenhaForte123!",
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)