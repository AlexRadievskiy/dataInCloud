from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from .models import Parent

class ParentModelTests(TestCase):
    def test_get_info(self):
        parent = Parent.objects.create(name='John Doe', age=30, email='john@example.com')
        self.assertEqual(parent.get_info(), 'John Doe, 30 years old')


class ParentAPITests(APITestCase):
    def test_create_parent(self):
        url = reverse('parent-list')
        data = {'name': 'John Doe', 'age': 30, 'email': 'john@example.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Parent.objects.count(), 1)
        self.assertEqual(Parent.objects.get().name, 'John Doe')

    def test_list_parents(self):
        Parent.objects.create(name='John Doe', age=30, email='john@example.com')
        url = reverse('parent-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
