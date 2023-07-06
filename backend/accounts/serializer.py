from dataclasses import field
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer


# from .views import send_confirmation_email
from .models import CustomUser, Profile
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from rest_framework import serializers

class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD


  

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        # model = get_user_model()
        model = CustomUser
        fields = ('first_name', 'last_name','email','password')

class ProfileSerializer(serializers.ModelSerializer):
   # user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'



#*************************

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, email):
        user = get_user_model().objects.filter(email=email).first()
        # user = CustomUser.objects.filter(email=email).first()
   
        if not user:
            raise serializers.ValidationError({'email': 'User does not exist'})
        return email
    
from django.contrib.auth.password_validation import validate_password



class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    
class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)
    confirm_password = serializers.CharField(max_length=128)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    