from .models import Campaign, Restaurant
from rest_framework import serializers


class RestaurantSerializer(serializers.ModelSerializer):
     class Meta:
        model = Restaurant
        fields ='__all__'



class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'
    #  'end_date': '2023-07-31',