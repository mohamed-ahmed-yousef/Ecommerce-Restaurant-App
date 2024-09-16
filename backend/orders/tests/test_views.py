from django.utils import timezone
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import CustomUser
from restaurants.models import Restaurant
from orders.models import DeliveryCharge, Order, OrderItem
from orders.serializers import DeliveryChargeSerializer, OrderSerializer, OrderItemSerializer
from products.models import Product  # Assuming you have a Product model in the products app

class OrderViewTestCase(APITestCase):
    def setUp(self):
        # Create some test data
        self.restaurant = Restaurant.objects.create(name='Test Restaurant', rate=3.0,location='123 Main St',road='address',city='city')
        self.customer = CustomUser.objects.create(email='testuser@example.com', password='adminpassword')
        self.product = Product.objects.create(name="Test Product", price=10.00, available_quantity=100,restaurant=self.restaurant)
        self.order = Order.objects.create(
            delivery_option="takeaway",
            time_preferred=timezone.now(),
            customer=self.customer,
            restaurant=self.restaurant,
            total_price=50.00
        )

        self.order_item = OrderItem.objects.create(
            order=self.order,
            item=self.product,
            quantity=3
        )
        self.delivery_charge = DeliveryCharge.objects.create(
            region="Test Region",
            charge=5.00,
            order=self.order
        )
    def authenticate_admin_user(self):
        # Create an admin user and authenticate the client
        self.admin_user = CustomUser.objects.create_superuser(email='admin@example.com', password='adminpassword')
        self.client.force_authenticate(user=self.admin_user)

    def authenticate_regular_user(self):
        # Create a regular user and authenticate the client
        self.regular_user = CustomUser.objects.create_user(email='regularuser@example.com', password='userpassword')
        self.client.force_authenticate(user=self.regular_user)

    def test_list_delivery_charges_authenticated(self):
        url = reverse('deliverycharge-list')
        self.authenticate_regular_user()  # Authenticate the client as a regular user
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_delivery_charge_viewset(self):
        # Test GET request to retrieve delivery charges
        self.client.login(email='testuser@example.com', password='adminpassword')
        url = reverse('deliverycharge-list')
        self.authenticate_regular_user()  # Authenticate the client as a regular user

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['region'], self.delivery_charge.region)


    def test_order_item_viewset(self):
        # Test GET request to retrieve order items
        url = reverse('orderitem-list')
        self.authenticate_regular_user()
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['quantity'], self.order_item.quantity)

    def test_order_viewset(self):
        # Test GET request to retrieve orders
        url = reverse('order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['delivery_option'], self.order.delivery_option)

    def test_order_with_item_viewset(self):
        # Test POST request to create an order with items
        url = reverse('orderwithitem-list')
        data = {
            "delivery_option": "Delivery",
            "time_preferred": timezone.now(),
            "customer": self.order.customer.id,
            "restaurant": self.order.restaurant.id,
            "total_price": 50.00,
            "order_items": [
                {
                    "item": self.product.id,
                    "quantity": 2
                }
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)
        self.assertEqual(OrderItem.objects.count(), 2)
        self.assertEqual(Order.objects.last().delivery_option, "Delivery")
        self.assertEqual(OrderItem.objects.last().quantity, 2)
