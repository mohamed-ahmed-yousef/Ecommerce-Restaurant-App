from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import CustomUser
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from rest_framework import status
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode

class Test_registr_View(TestCase):
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

from django.core import mail
class PasswordResetRequestViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
           
            email='test@example.com',
            password='testpassword',
        )

    def test_password_reset_request(self):
        url=reverse('password_reset')
        data = {
            'email': 'test@example.com',
        }
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'detail': 'Password reset email has been sent.'})

        # Verify that a password reset email was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Password Reset')

    def test_password_reset_request_invalid_email(self):
        url=reverse('password_reset')
        data = {
            'email': 'invalid@example.com',
        }
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'detail': 'User with this email address does not exist.'})


class PasswordResetViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            password='password123'
        )

    def test_password_reset_view(self):
        # Generate a password reset token for the test user
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(self.user)

        # Encode the user's ID for the URL parameter
  
        uidb64=urlsafe_base64_encode(force_bytes(self.user.pk))

        # Define the request data
        data = {
            'password': 'newpassword123',
            'confirm_password': 'newpassword123'
        }

        # Generate the URL for the password reset endpoint
        url = reverse('password_reset_confirm', args=[uidb64, token])

        # Make a POST request to reset the password
        response = self.client.post(url, data, format='json')

        # Check the response status code and content
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'detail': 'Password has been reset successfully.'})

        # Refresh the user object from the database
        self.user.refresh_from_db()

        # Check that the password has been updated
        self.assertTrue(self.user.check_password(data['password']))