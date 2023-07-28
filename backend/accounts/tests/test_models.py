from django.test import TestCase
from accounts.models import CustomUser,Profile
from django.db import models


class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(
            email='test@example.com',
            first_name='John',
            last_name='Doe',
            email_confirmed=True,
            profile_completed=True
        )

    def test_email_field(self):
        user = CustomUser.objects.get(id=1)
        field = user._meta.get_field('email')
        self.assertEqual(field.verbose_name, 'email address')
        self.assertTrue(field.unique)


    
    # def test_first_name_field(self):
    #     user = CustomUser.objects.get(id=1)
    #     field = user._meta.get_field('first_name')
    #     self.assertEqual(field.max_length, 50)
    #     self.assertFalse(field.blank)

    # def test_last_name_field(self):
    #     user = CustomUser.objects.get(id=1)
    #     field = user._meta.get_field('last_name')
    #     self.assertEqual(field.max_length, 50)
    #     self.assertFalse(field.blank)

    def test_email_confirmed_field(self):
        user = CustomUser.objects.get(id=1)
        field = user._meta.get_field('email_confirmed')
        self.assertEqual(field.verbose_name, 'email confirmed')
        self.assertFalse(field.default)

    def test_profile_completed_field(self):
        user = CustomUser.objects.get(id=1)
        field = user._meta.get_field('profile_completed')
        self.assertFalse(field.default)

    def test_str_method(self):
        user = CustomUser.objects.get(id=1)
        expected_str = user.email
        self.assertEqual(str(user), expected_str)




class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create(
            email='test@example.com',
            first_name='John',
            last_name='Doe',
            email_confirmed=True,
            profile_completed=True
        )
        Profile.objects.create(
            user=user,
            bio='Test bio',
            date_of_birth='2000-01-01',
            phone_number='1234567890'
        )

    def test_user_field(self):
        profile = Profile.objects.get(id=1)
        field = profile._meta.get_field('user')
        self.assertIsInstance(field, models.OneToOneField)
        self.assertEqual(field.remote_field.model, CustomUser)
        self.assertTrue(field.unique)

    def test_bio_field(self):
        profile = Profile.objects.get(id=1)
        field = profile._meta.get_field('bio')
        self.assertTrue(field.blank)

    def test_profile_image_field(self):
        profile = Profile.objects.get(id=1)
        field = profile._meta.get_field('profile_image')
        self.assertIsInstance(field, models.ImageField)
        self.assertEqual(field.upload_to, 'profile_pictures/')
        self.assertTrue(field.blank)
        self.assertTrue(field.null)

    def test_date_of_birth_field(self):
        profile = Profile.objects.get(id=1)
        field = profile._meta.get_field('date_of_birth')
        self.assertIsInstance(field, models.DateField)
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_phone_number_field(self):
        profile = Profile.objects.get(id=1)
        field = profile._meta.get_field('phone_number')
        self.assertEqual(field.max_length, 20)
        self.assertTrue(field.null)
        self.assertTrue(field.blank)

    def test_str_method(self):
        profile = Profile.objects.get(id=1)
        expected_str = profile.user.first_name
        self.assertEqual(str(profile), expected_str)
