from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from .views import CampaignViewSet, CategoryViewSet, DiscountViewSet, ProductViewSet, RestaurantViewSet, index

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('discounts', DiscountViewSet)
router.register('restaurent', RestaurantViewSet)
router.register('products', ProductViewSet)
router.register('campaigns', CampaignViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index.as_view(), name='index'),
]
