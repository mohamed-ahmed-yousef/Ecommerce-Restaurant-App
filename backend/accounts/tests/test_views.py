from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import CustomUser
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from rest_framework import status
from django.contrib.auth import get_user_model, authenticate

class TestView(TestCase):
    def setUp(self) :
        self.client = Client()
        self.user = CustomUser.objects.create(email='test@example.com')
        self.uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        self.token = default_token_generator.make_token(self.user)


    def test_registr_post(self):
        url=reverse('register')
        response = self.client.post(url,{'email': 'test@gmail.com', 
                        'password': 'testtest','first_name': 'test', 'last_name': 'test'})
        self.assertEqual(response.status_code, 201)
        

class EmailConfirmationViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create(email='test@example.com')
        self.uidb64 = urlsafe_base64_encode(force_bytes(self.user.pk))
        self.token = default_token_generator.make_token(self.user)

    def test_email_confirmation_valid_link(self):
        url = reverse('email-confirmation', kwargs={'uidb64': self.uidb64, 'token': self.token})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Email confirmed successfully.'})

        # Assert that the user's email_confirmed field is updated
        self.user.refresh_from_db()
        self.assertTrue(self.user.email_confirmed)

    def test_email_confirmation_invalid_token(self):
        invalid_token = 'invalid_token'
        url = reverse('email-confirmation', kwargs={'uidb64': self.uidb64, 'token': invalid_token})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Invalid token.'})

    def test_email_confirmation_invalid_link(self):
        invalid_uidb64 = 'invalid_uidb64'
        url = reverse('email-confirmation', kwargs={'uidb64': invalid_uidb64, 'token': self.token})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Invalid link.'})

    def test_email_confirmation_missing_user(self):
        self.user.delete()
        url = reverse('email-confirmation', kwargs={'uidb64': self.uidb64, 'token': self.token})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Invalid link.'})




User = get_user_model()

from django.test import TestCase
from rest_framework import status

# from accounts.views import EmailTokenObtainPairView
# from django.contrib.auth.models import User

class EmailTokenObtainPairViewTest(TestCase):
    def setUp(self):
        self.client  =  Client()
        self.user = CustomUser.objects.create(
            email='test@example.com',
            password='testpassword',
            first_name='test',
            last_name='test',
            # is_superuser=False,
            # email_confirmed=True
        )

    def test_obtain_auth_token(self):
        data = {
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        url=reverse('token_obtain_pair')
        response = self.client.post(url,data)

        self.assertEqual(response.status_code, 200)
        # self.assertIn('access', response.data)
        # self.assertIn('refresh', response.data)
        # self.assertEqual(str(self.user.refresh_token.access_token), response.data['access'])
        # self.assertEqual(str(self.user.refresh_token), response.data['refresh'])

#     def test_obtain_auth_token_incorrect_credentials(self):
#         data = {
#             'email': 'test@example.com',
#             'password': 'wrongpassword'
#         }
#         request = self.factory.post('/auth/token/', data=data)
#         response = self.view(request)

#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.data, {'error': 'Incorrect email or password'})

#     def test_obtain_auth_token_unconfirmed_email(self):
#         self.user.email_confirmed = False
#         self.user.save()

#         data = {
#             'email': 'test@example.com',
#             'password': 'testpassword'
#         }
#         request = self.factory.post('/auth/token/', data=data)
#         response = self.view(request)

#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.data, {'error': 'Email is not confirmed'})
#         # self.assertEqual(response.data, {'error': [{'error': 'Email is not confirmed', 'code': 'invalid'}]})
