#urls.py django


from django.urls import include, path
from rest_framework import routers

from .views import DeliveryChargeViewSet, OrderViewSet
router=routers.DefaultRouter()
router.register('delivery_charge', DeliveryChargeViewSet)
router.register('order', OrderViewSet)

urlpatterns = [

    path('', include(router.urls)),
    
]
