from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, DiscountViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('discounts', DiscountViewSet)
router.register('products', ProductViewSet)

urlpatterns = [
    # Other URL patterns
    path('', include(router.urls)),
]
