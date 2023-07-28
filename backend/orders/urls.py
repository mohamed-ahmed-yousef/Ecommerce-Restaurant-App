#urls.py django


from django.urls import include, path
from rest_framework import routers

from .views import DeliveryChargeViewSet, OrderViewSet, OrderwithItemViewSet, OrderItemViewSet
router=routers.DefaultRouter()
router.register('delivery_charge', DeliveryChargeViewSet)
router.register('order_with_items', OrderwithItemViewSet)
router.register('orders', OrderViewSet)
router.register('order_items', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]
