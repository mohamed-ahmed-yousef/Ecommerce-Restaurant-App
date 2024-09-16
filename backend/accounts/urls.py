from django.urls import include, path
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
# from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView, LogoutView , PasswordResetView, PasswordResetConfirmView 

urlpatterns = [
    # Other URL patterns
    path('register/', RegisterView.as_view(), name='register'),


    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),

    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('', include('dj_rest_auth.urls')),
    path('', include('allauth.urls')),
]
