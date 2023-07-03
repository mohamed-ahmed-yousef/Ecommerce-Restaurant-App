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

# from .tokens import account_activation_token




# class UserViewSet(viewsets.ViewSet):
#     def create(self, request):
#         # Process registration form and save user data
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()

#             # Send confirmation email
#             send_confirmation_email(user)

#             return Response({'message': 'User registered successfully. Please check your email for confirmation.'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        print('@'*50)
        if user and not user.email_confirmed:
            send_confirmation_email(user,get_current_site(self.request))
            raise InvalidToken('Email address not confirmed. Please verify your email.')
        # elif  user.profile_completed :
        #     raise InvalidToken(' profile not completed. Please complete your profile.')

        return data
    
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
        mutable_data['user'] = request.user.id
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)
    # def create(self, request, *args, **kwargs):
    #     request.data['user'] = request.user.id
    #     print('*'*100)
    #     return super().create(request, *args, **kwargs)


# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]











    # def create(self, request, *args, **kwargs):
    #     print('*'*50)
    #     token, created = Token.objects.get_or_create(user=request.user)
    #     print(token.key)  
    #     if request.user.is_authenticated:
    #         print(request.user.email)
    #         # print(request.user.password)
    #         # User is authenticated
            
    #         return super().create(request, *args, **kwargs)
    #     else:
    #         # User is not authenticated
    #         return Response({"message": "Not Authenticated"}, status=HTTP_401_UNAUTHORIZED)
    # http_method_names = ["post"]
    # def post(self,request, *args, **kwargs):
    #     print('*'*50)
    # def get_permissions(self):
    #     print(self.request)
    #     if self.action == 'create':
    #         return [permissions.AllowAny()]

    #     if  self.request.method == 'GET':
    #         self.permission_classes = [permissions.IsAdminUser]