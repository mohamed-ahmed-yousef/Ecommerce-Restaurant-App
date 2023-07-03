from django.urls import include, path

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

from .views import EmailTokenObtainPairView, ProfileViewSet, RegisterView,EmailConfirmationView

router = routers.DefaultRouter()
router.register('profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='token_obtain_pair'),
    path('token/obtain/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('confirm-email/<str:uidb64>/<str:token>/', EmailConfirmationView.as_view(), name='email-confirmation'),
   
    path('', include( router.urls)),
]