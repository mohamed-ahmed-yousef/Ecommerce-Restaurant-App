from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from .views import CampaignViewSet, RestaurantViewSet

router = routers.DefaultRouter()
router.register('restaurent', RestaurantViewSet)
router.register('campaigns', CampaignViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
