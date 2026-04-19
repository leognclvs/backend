from rest_framework import status
from rest_framework.test import APITestCase

from core.accounts.models import User


class AuthViewsAPITest(APITestCase):
    def test_register_user_via_auth_endpoint(self):
        payload = {
            "email": "leo@example.com",
            "username": "leo",
            "display_name": "Leonardo",
            "password": "SenhaForte123!",
            "password_confirm": "SenhaForte123!",
        }

        response = self.client.post("/api/v1/auth/register/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().display_name, "Leonardo")
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("user", response.data)

    def test_forgot_password_endpoint(self):
        response = self.client.post(
            "/api/v1/auth/forgot-password/",
            {"email": "nobody@example.com"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("detail", response.data)
