from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.views import EmailTokenObtainPairView
from accounts.serializer import ObtainAuthTokenSerializer
from accounts.models import CustomUser, Profile


class EmailTokenObtainPairViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
     
            password='testpassword',
            email='test@example.com',
            email_confirmed=True
        )
       
        self.url = reverse('tokenOBtain')
  
    def test_token_obtain_pair(self):
        data = {
            'email': 'test@example.com',
            'password': 'testpassword'
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    
class ProfileViewSetTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list_profiles(self):
        url = reverse('profile-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_create_profile(self):
    #     # url = 'http://127.0.0.1:8000/accounts/profiles/'
    #     url=reverse('profile-list')
    #     data = {
    #         'name': 'John Doe',
    #         'email': 'john@example.com',
    #         'bio': 'A test profile',
    #     }
    #     response = self.client.post(url, data)

    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Profile.objects.count(), 1)
    #     self.assertEqual(Profile.objects.get().name, 'John Doe')

    # def test_retrieve_profile(self):
    #     profile = Profile.objects.create(email='john@example.com', bio='A test profile')
    #     url = reverse('profile-detail', args=[profile.id])
    #     response = self.client.get(url)

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['name'], 'John Doe')

    # def test_update_profile(self):
    #     profile = Profile.objects.create(name='John Doe', email='john@example.com', bio='A test profile')
    #     url = reverse('profile-detail', args=[profile.id])
    #     data = {
    #         'name': 'Updated Name',
    #         'email': 'updated@example.com',
    #         'bio': 'Updated bio',
    #     }
    #     response = self.client.put(url, data)

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Profile.objects.get().name, 'Updated Name')

    # def test_delete_profile(self):
    #     profile = Profile.objects.create(name='John Doe', email='john@example.com', bio='A test profile')
    #     url = reverse('profile-detail', args=[profile.id])
    #     response = self.client.delete(url)

    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(Profile.objects.count(), 0)