from django.urls import path, include
from rest_framework import routers

from .views import  CategoryViewSet, DiscountViewSet, ProductViewSet, index

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('discounts', DiscountViewSet)
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index.as_view(), name='index'),
]
