from django.shortcuts import render
from django.contrib.auth import get_user_model

from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework import viewsets,permissions,generics

from .models import Profile
from .serializer import ProfileSerializer, UserSerializer, TokenObtainPairSerializer ,send_confirmation_email
from django.contrib.auth import authenticate
User = get_user_model()
from django.core.mail import EmailMessage

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

class RegisterView(APIView):
    http_method_names = ['post']

    def post(self, request,*args, **kwargs):
        serializer = UserSerializer(data=self.request.data)
        if serializer.is_valid():
            user=get_user_model().objects.create_user(**serializer.validated_data)
          # Send confirmation email
            # if not request.user.is_staff:
            send_confirmation_email(user,request)
            # return Response(status=HTTP_201_CREATED)
            return Response({'message': 'User registered successfully. Please check your email for confirmation.'}, status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

from rest_framework_simplejwt.tokens import RefreshToken
class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            email= request.data['email']
            password= request.data['password']
            user=authenticate(email=email, password=password)
          
     
            if (not user.email_confirmed and not user.is_superuser):
                return Response({'error': 'Email is not confirmed'}, status=HTTP_400_BAD_REQUEST)

            token = RefreshToken.for_user(serializer.user)
            return Response({
                'access': str(token.access_token),
                'refresh': str(token)
            })

    
class EmailConfirmationView(generics.GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                user.email_confirmed = True
                user.save()
                return Response({'message': 'Email confirmed successfully.'})
            else:
                return Response({'message': 'Invalid token.'})
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({'message': 'Invalid link.'})
        
from copy import deepcopy

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        mutable_data = deepcopy(request.data)

        user=request.user
        user.profile_completed=True
        user.save()

        mutable_data['user'] =user.id
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)


