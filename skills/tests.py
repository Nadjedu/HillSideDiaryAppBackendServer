from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Skills


class UserModelCreationTestCase(TestCase):
    def test_create_regular_user_success(self):
        skill = User.objects.create_skill(record_number='123', client_id='1234', skill_code='12', skill_description = 'Test',
        note ='Testing',date_added='01/01/2021',date_modified='01/02/2021' ,active=True)
        self.assertTrue(isinstance(skill, Skill))

class SkillsApiTest(APITestCase):
    def test_create_skill(self):
        """
        Ensure we can create a new account.
        """
        data = {
            'record_number': '123', 'client_id':'1234', 'skill_code':'12', 'skill_description' : 'Test',
        'note' :'Testing','date_added':'01/01/2021','date_modified': '01/02/2021' ,'active': True
        }
        url = reverse("user-list")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Skills.objects.count(), 1)
