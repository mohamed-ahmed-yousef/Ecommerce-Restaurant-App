from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.views import EmailTokenObtainPairView
from backend.accounts.serializers import ObtainAuthTokenSerializer
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
from rest_framework.authtoken.models import Token
from django.test import TestCase, RequestFactory

from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
class ProfileViewSetTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = CustomUser.objects.create_user(email='johndoe@example.com', password='testpassword')

    def test_create_profile(self):
        # self.client.force_login(self.user)
        url='/accounts/profile/'
        data = {
#             # 'user': {
                'first_name': 'John',
                'last_name': 'Doe',
                # 'email': 'johndoe@example.com'
#             # },
#             # Other profile data
        }
        token = Token.objects.create(user=self.user)
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        # self.client.defaults['HTTP_AUTHORIZATION'] = 'Token ' + token.key
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # profile = Profile.objects.get(name='John Doe')
        # self.assertEqual(profile.user.id, self.user.id)

# class ProfileViewSetTestCase(TestCase):
#     def setUp(self):
#         # self.client = Client()
#         self.factory = APIRequestFactory()
#         self.user = CustomUser.objects.create_user(email='johndoe@gamil.com', password='testpass')

#     def test_create_profile_with_user_update(self):
        
#         # Create profile with user update data
#         data = {
#             # 'user': {
#                 'first_name': 'John',
#                 'last_name': 'Doe',
#                 'ursr': 'johndoe@example.com'
#             # },
#             # Other profile data
#         }
#         # url=reverse('profile')
#         url='/accounts/profile/'
#         self.token = Token.objects.create(user=self.user)
#         request = self.factory.pst(url,data)
#         force_authenticate(request, user=self.user, token=self.token)

#         response = self.client.get(url, format='json')
#         # force_authenticate(request, user=self.user, token=self.token)
#         # response = self.client.post(url, data,self.token, format='json')



#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         # profile = Profile.objects.get(user=self.user)
#         # self.assertEqual(profile.user.first_name, 'John')
#         # self.assertEqual(profile.user.last_name, 'Doe')
#         # self.assertEqual(profile.user.email, 'johndoe@example.com')