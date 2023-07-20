from django.contrib.auth import get_user_model

from django.utils.encoding import  force_str 
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import  urlsafe_base64_decode

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets,permissions,generics ,status

from .sendEmail import send_confirmation_email, send_password_reset_email

from .models import  Profile
from .serializers import  ObtainAuthTokenSerializer, PasswordResetRequestSerializer, PasswordResetSerializer, ProfileSerializer, UserSerializer 
from django.contrib.auth import authenticate
User = get_user_model()

from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str


class RegisterView(generics.GenericAPIView):
    serializer_class=UserSerializer
    def post(self, request,*args, **kwargs):
        # print('*'*100)
        # print(request)
        serializer = UserSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user=get_user_model().objects.create_user(**serializer.validated_data)
        # serializer.save()
        # user = User.objects.get(email=serializer.data['email'])
        # send_confirmation_email(user, get_current_site(request))
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
    

class EmailTokenObtainPairView(TokenObtainPairView):
        serializer_class = ObtainAuthTokenSerializer
        def post(self, request):
            serializer = ObtainAuthTokenSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = authenticate(**serializer.validated_data)
            token = RefreshToken.for_user(user)
            context={
                'access': str(token.access_token),
                'refresh': str(token)
            }
            
            return Response(data=context, status=status.HTTP_200_OK)
          
        def get(self, request,*args, **kwargs):
            print('*'*100)
            print('get')
class EmailConfirmationView(generics.GenericAPIView):
    def get_serializer(self):
        return 
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
        

class PasswordResetRequestView(APIView):
    serializer_class = PasswordResetRequestSerializer
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'User with this email address does not exist.'}, status=400)

        send_password_reset_email(user,get_current_site(request))
        return Response({'detail': 'Password reset email has been sent.'},status.HTTP_200_OK)
    

class PasswordResetView(generics.GenericAPIView):
    serializer_class=PasswordResetSerializer
    def post(self, request,uidb64, token,*args,**kwargs):
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        id = smart_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=id)
        if not PasswordResetTokenGenerator().check_token(user, token):
            return Response({'detail': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
                   
        password = serializer.validated_data['password']
        user.set_password(password)
        user.save()

        return Response({'detail': 'Password has been reset successfully.'})
    

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

 
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] =  self.request.user.id
        return context
    
    def create(self, request, *args, **kwargs):
       
        serializer = ProfileSerializer(data=self.get_serializer_context())
        # serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
