from dataclasses import field
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer
from .models import Profile

class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # field='__all__'
        fields = ['id','bio', 'profile_image', 'date_of_birth', 'phone_number']
        # fields = ['id', 'first_name', 'last_name', 'bio', 'profile_image', 'date_of_birth', 'phone_number']