from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import EmailTokenObtainPairView, ProfileViewSet, RegisterView

from rest_framework import routers

router = routers.DefaultRouter()
router.register('profiles', ProfileViewSet, basename='profile')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='token_obtain_pair'),
    path('token/obtain/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include( router.urls)),
]