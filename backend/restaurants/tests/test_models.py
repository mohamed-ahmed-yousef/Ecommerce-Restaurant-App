from django.test import TestCase
from restaurants.models import Restaurant, Campaign

class RestaurantModelTest(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name='Test Restaurant',
            location='Test Location',
            house='Test House',
            road='Test Road',
            city='Test City',
            delivery_time='30 minutes',
            min_order=20,
            rate=4,
        )

    def test_restaurant_str_method(self):
        self.assertEqual(str(self.restaurant), 'Test Restaurant')

class CampaignModelTest(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name='Test Restaurant',
            location='Test Location',
            house='Test House',
            road='Test Road',
            city='Test City',
            delivery_time='30 minutes',
            min_order=20,
            rate=4,
        )

        self.campaign = Campaign.objects.create(
            name='Test Campaign',
            end_date='2023-12-31',
            description='Test Campaign Description',
            image='test_image.jpg',
        )
        self.campaign.restaurant.add(self.restaurant)

    def test_campaign_str_method(self):
        self.assertEqual(str(self.campaign), 'Test Campaign')
    
    def test_campaign_restaurant_relationship(self):
        self.assertEqual(self.campaign.restaurant.count(), 1)
        self.assertEqual(self.campaign.restaurant.first().name, 'Test Restaurant')

