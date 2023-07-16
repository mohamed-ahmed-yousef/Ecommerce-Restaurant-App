
from rest_framework import viewsets

from .models import Campaign ,Restaurant
from .serializers import CampaignSerializer, RestaurantSerializer

# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class=RestaurantSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer