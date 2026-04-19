from rest_framework import status
from rest_framework.test import APITestCase

from core.accounts.models import User


class AuthTokenAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="leo@example.com",
            username="leo",
            display_name="Leonardo",
            password="SenhaForte123!",
        )

    def test_login_returns_tokens_and_user(self):
        payload = {
            "email": "leo@example.com",
            "password": "SenhaForte123!",
        }

        response = self.client.post("/api/v1/auth/login/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertEqual(response.data["user"]["email"], "leo@example.com")

    def test_me_and_change_password_flow(self):
        login_response = self.client.post(
            "/api/v1/auth/login/",
            {"email": "leo@example.com", "password": "SenhaForte123!"},
            format="json",
        )
        access = login_response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")

        me_response = self.client.get("/api/v1/auth/me/")
        self.assertEqual(me_response.status_code, status.HTTP_200_OK)
        self.assertEqual(me_response.data["username"], "leo")

        change_response = self.client.post(
            "/api/v1/auth/change-password/",
            {
                "current_password": "SenhaForte123!",
                "new_password": "NovaSenha123!",
                "new_password_confirm": "NovaSenha123!",
            },
            format="json",
        )
        self.assertEqual(change_response.status_code, status.HTTP_200_OK)

        self.client.credentials()
        relogin = self.client.post(
            "/api/v1/auth/login/",
            {"email": "leo@example.com", "password": "NovaSenha123!"},
            format="json",
        )
        self.assertEqual(relogin.status_code, status.HTTP_200_OK)
