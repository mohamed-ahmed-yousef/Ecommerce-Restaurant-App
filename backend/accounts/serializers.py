from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError

from dj_rest_auth.serializers import PasswordResetSerializer
from django.contrib.sites.models import Site
from dj_rest_auth.serializers import PasswordResetSerializer

class CustomPasswordResetSerializer(PasswordResetSerializer):
    def get_email_options(self):
        current_site = Site.objects.get_current()
        return {
            'subject_template_name': 'path/to/password_reset_subject.txt',
            'email_template_name': 'path/to/password_reset_email.txt',
            'html_email_template_name': 'path/to/password_reset_email.html',
            'extra_email_context': {
                'user': self.user,
                'site_domain': current_site.domain,
                'site_name': current_site.name,
            },
        }
