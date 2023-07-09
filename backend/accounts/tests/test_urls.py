from django.test import SimpleTestCase
from django.urls import resolve, reverse

from accounts.views import EmailTokenObtainPairView, RegisterView


class TestUrls(SimpleTestCase):
    def test_register_url_resolver(self):
        url=reverse('register')
        self.assertEqual(resolve(url).func.view_class,RegisterView)
    def test_obtain_url_resolver(self):
        url=reverse('tokenOBtain')
        self.assertEqual(resolve(url).func.view_class,EmailTokenObtainPairView)
        # url=reverse('tokenOBtain')
