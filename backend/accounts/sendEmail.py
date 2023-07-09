from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str 
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from .models import CustomUser

from rest_framework_simplejwt.tokens import RefreshToken

def send_email(user,current_site,file_link,mail_subject,token):
   
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    # current_site = get_current_site(request)
    message = render_to_string(file_link, {
        'user': user,
        'domain': current_site.domain,
        'uid': uid,
        'token': token
    })
    email = EmailMessage(mail_subject, message, to=[user.email])
    email.content_subtype = 'html'  
    email.send()

def send_confirmation_email(user,current_site):
    # token = default_token_generator.make_token(user)
    token= RefreshToken.for_user(user).access_token
    mail_subject = 'Activate your account'
    file_link='/run/media/mohamed/New Volume/Documents/programing/django/restaurant/Ecommerce-Restaurant-App/backend/accounts/templates/activation_email.html'
    send_email(user,current_site,file_link,mail_subject,token)


from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework.authtoken.models import Token
def send_password_reset_email(user,current_site):
    token = PasswordResetTokenGenerator().make_token(user)
    mail_subject = 'Password Reset'
    file_link='password_reset_email.html'
    send_email(user,current_site,file_link,mail_subject,token)


