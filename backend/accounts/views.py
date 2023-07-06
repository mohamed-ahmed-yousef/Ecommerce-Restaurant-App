from django.conf import settings
from django.contrib.auth import get_user_model

from django.utils.encoding import force_bytes, force_str 
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets,permissions,generics ,status

from .sendEmail import send_confirmation_email, send_password_reset_email

from .models import CustomUser, Profile
from .serializer import  PasswordResetRequestSerializer, PasswordResetSerializer, ProfileSerializer, UserSerializer, TokenObtainPairSerializer 
from django.contrib.auth import authenticate
User = get_user_model()
from django.core.mail import EmailMessage

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from copy import deepcopy





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
            return Response({'message': 'User registered successfully. Please check your email for confirmation.'}, status=status.statusHTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'errors': serializer.errors})

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            email= request.data['email']
            password= request.data['password']
            user=authenticate(email=email, password=password)
          
     
            if (not user.email_confirmed and not user.is_superuser):
                return Response({'error': 'Email is not confirmed'}, status=status.HTTP_400_BAD_REQUEST)

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
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# class PasswordResetView(generics.GenericAPIView):
#     def post(self, request):
#         email = request.data.get('email')

#         user = User.objects.get(email=email)
#         if user:
#             # Generate reset token
#             token = default_token_generator.make_token(user)

#             # Build reset password URL
#             uid = urlsafe_base64_encode(force_bytes(user.pk))
#             current_site = get_current_site(request)

#             # Send reset password email
#             subject = 'Password Reset'
#             # reset_url = f"{current_site}/accounts/reset-password/{uid}/{token}/"
#             message = render_to_string('password_reset_email.html', {
#                 'user': user,
#                  'uid': uid,
#                  'token': token,
#                  'current_site': current_site
#             })
#             # send_mail(subject, message, 'noreply@example.com', [user.email])
#             email = EmailMessage(subject, message, to=[user.email])
#             email.content_subtype = 'html'  
#             email.send()

       
#         return Response(status=status.HTTP_200_OK)


# class PasswordResetViewSet(viewsets.ViewSet):
#     serializer_class = PasswordResetSerializer
#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         email = serializer.validated_data['email']
#         send_password_reset_email(email,request)
#         return Response({'success': 'Password reset email sent'})
class PasswordResetRequestView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'User with this email address does not exist.'}, status=400)

        send_password_reset_email(user,request)
        return Response({'detail': 'Password reset email has been sent.'})
    
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str
class PasswordResetView(generics.GenericAPIView):
    def post(self, request,uidb64, token,*args,**kwargs):
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Verify the token's authenticity and validity
        # user = User.objects.get(verification_token=token)
        id = smart_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=id)
        if not PasswordResetTokenGenerator().check_token(user, token):
            return Response({'detail': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
                   
        password = serializer.validated_data['password']
        user.set_password(password)
        user.save()

        return Response({'detail': 'Password has been reset successfully.'})