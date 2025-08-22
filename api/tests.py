from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Teacher

class SmokeTest(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser('admin','a@a.com','pass1234')

    def test_public_can_list_teachers(self):
        Teacher.objects.create(name='T1', email='t1@ex.com')
        url = reverse('teacher-list')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_admin_can_create_teacher(self):
        token_url = reverse('token_obtain_pair')
        res = self.client.post(token_url, {'username':'admin','password':'pass1234'})
        access = res.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        url = reverse('teacher-list')
        res = self.client.post(url, {'name':'T2','email':'t2@ex.com','specialization':'Sci'})
        self.assertEqual(res.status_code, 201)

