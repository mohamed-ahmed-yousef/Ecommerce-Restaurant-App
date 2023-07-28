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
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

class ObtainAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    def validate(self, data):
        user = authenticate(**data)
        if user is None:
            raise serializers.ValidationError({'error': 'Incorrect email or password'})
        # if (not user.email_confirmed and not user.is_superuser):
        #     raise serializers.ValidationError({'error': 'Email is not confirmed'})
        data['token'] =RefreshToken.for_user(user)
        return data
    
    
# class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
#     username_field = get_user_model().USERNAME_FIELD



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    class Meta:
        model = CustomUser
        fields = ('name','email','password')
        # fields = '__all__'
    def to_representation(self, instance):
        """
        Exclude the password field when serializing the User object.
        """
        data = super().to_representation(instance)
        data.pop('password', None)
        return data
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
    
    def create(self, validated_data):
            profile = Profile.objects.create(**validated_data)           
            user = profile.user
            user.profile_completed = True
            user.save()
            return profile





class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)
    confirm_password = serializers.CharField(max_length=128)

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    