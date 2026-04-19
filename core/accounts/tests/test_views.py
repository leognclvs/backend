from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.accounts.models import User


class UserRegistrationAPITest(APITestCase):
    def test_create_user(self):
        url = reverse("user-list")
        payload = {
            "email": "leo@example.com",
            "username": "leo",
            "display_name": "Leonardo",
            "password": "SenhaForte123!",
            "password_confirm": "SenhaForte123!",
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().email, "leo@example.com")