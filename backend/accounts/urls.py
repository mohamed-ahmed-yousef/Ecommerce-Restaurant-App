from django.urls import include, path

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

from .views import EmailTokenObtainPairView,PasswordResetRequestView, PasswordResetView, ProfileViewSet, RegisterView,EmailConfirmationView

router = routers.DefaultRouter()
router.register('profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/obtain/', EmailTokenObtainPairView.as_view(), name='tokenOBtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('confirm-email/<str:uidb64>/<str:token>/', EmailConfirmationView.as_view(), name='email-confirmation'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('reset-password/<uidb64>/<token>/', PasswordResetView.as_view(), name='password_reset_confirm'),
    path('', include( router.urls)),
    
]