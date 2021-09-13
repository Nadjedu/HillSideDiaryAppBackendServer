from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class UserModelCreationTestCase(TestCase):
    def test_create_regular_user_success(self):
        user = User.objects.create_user(email="test@test.com", password="123")
        self.assertTrue(isinstance(user, User))

    def test_create_regular_user_unsuccessful(self):
        user = User.objects.create_user(email="test@test.com")
        self.assertFalse(isinstance(user, User))

    def test_create_super_user_success(self):
        user = User.objects.create_superuser(email="test@test.com", password="123")
        self.assertTrue(isinstance(user, User))

    def test_create_regular_super_user_unsuccessful(self):
        user = User.objects.create_superuser(email="test@test.com")
        self.assertFalse(isinstance(user, User))


class AccountsAPITest(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account.
        """
        data = {
            "email": "test99@test99.com",
            "password": "123"
        }
        url = reverse("user-list")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(response.has_header('token'))
