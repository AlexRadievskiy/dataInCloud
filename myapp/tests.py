from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from .models import Parent

# Unit tests for the Parent model
class ParentModelTests(TestCase):
    def test_get_info(self):
        parent = Parent.objects.create(name='John Doe', age=30, email='john@example.com')
        self.assertEqual(parent.get_info(), 'John Doe, 30 years old')

    def test_parent_age_validation(self):
        with self.assertRaises(Exception):
            Parent.objects.create(name='John Doe', age=17, email='john@example.com')

    def test_parent_name_max_length(self):
        parent = Parent.objects.create(name='A' * 100, age=30, email='john@example.com')
        self.assertEqual(parent.name, 'A' * 100)

        with self.assertRaises(Exception):
            Parent.objects.create(name='A' * 101, age=30, email='john@example.com')

    def test_parent_email_validation(self):
        parent = Parent.objects.create(name='John Doe', age=30, email='john@example.com')
        self.assertEqual(parent.email, 'john@example.com')

        with self.assertRaises(Exception):
            Parent.objects.create(name='John Doe', age=30, email='invalid-email')

# Integration tests for the Parent API
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
        self.assertEqual(response.data[0]['name'], 'John Doe')

    def test_retrieve_parent(self):
        parent = Parent.objects.create(name='John Doe', age=30, email='john@example.com')
        url = reverse('parent-detail', args=[parent.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John Doe')

    def test_update_parent(self):
        parent = Parent.objects.create(name='John Doe', age=30, email='john@example.com')
        url = reverse('parent-detail', args=[parent.id])
        data = {'name': 'Jane Doe', 'age': 32, 'email': 'jane@example.com'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        parent.refresh_from_db()
        self.assertEqual(parent.name, 'Jane Doe')
        self.assertEqual(parent.age, 32)
        self.assertEqual(parent.email, 'jane@example.com')

    def test_delete_parent(self):
        parent = Parent.objects.create(name='John Doe', age=30, email='john@example.com')
        url = reverse('parent-detail', args=[parent.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Parent.objects.count(), 0)
