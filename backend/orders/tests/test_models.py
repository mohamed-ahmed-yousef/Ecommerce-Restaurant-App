from django.test import TestCase
from django.utils import timezone
from orders.models import OrderItem, DeliveryCharge, Order
from orders.serializers import OrderSerializer, OrderItemSerializer, DeliveryChargeSerializer
from products.models import Product  # Import Product model if not already imported
from accounts.models import CustomUser  # Import CustomUser model if not already imported
from restaurants.models import Restaurant  # Import Restaurant model if not already imported

class OrderModelTestCase(TestCase):
    def setUp(self):
        # Create a test restaurant
        self.restaurant = Restaurant.objects.create(name='Test Restaurant', rate=3.0,location='123 Main St',road='address',city='city')

        # Create a test customer
        self.customer = CustomUser.objects.create(email='testuser@example.com')


        # Create a test order
        self.order = Order.objects.create(
            delivery_option="takeaway",
            time_preferred=timezone.now(),
            customer=self.customer,
            restaurant=self.restaurant,
            total_price=50.00
        )

    def test_order_creation(self):
        """Test the creation of a new Order instance."""
        self.assertIsInstance(self.order, Order)
        self.assertEqual(Order.objects.count(), 1)

    def test_order_delivery_option_choices(self):
        """Test that the delivery option choices are valid."""
        delivery_options = [choice[0] for choice in self.order._meta.get_field('delivery_option').choices]
        self.assertIn("takeaway", delivery_options)

    def test_order_customer_relationship(self):
        """Test the relationship between Order and CustomUser."""
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.customer.order_set.first(), self.order)

    def test_order_restaurant_relationship(self):
        """Test the relationship between Order and Restaurant."""
        self.assertEqual(self.order.restaurant, self.restaurant)
        self.assertEqual(self.restaurant.order_set.first(), self.order)

    def test_order_total_price(self):
        """Test the total price of the order."""
        self.assertEqual(self.order.total_price, 50.00)

    def test_order_time_preferred(self):
        """Test the preferred delivery time."""
        self.assertIsNotNone(self.order.time_preferred)


class OrderItemModelTestCase(TestCase):
    def setUp(self):
        # Create a test order
        self.restaurant = Restaurant.objects.create(name='Test Restaurant', rate=3.0,location='123 Main St',road='address',city='city')

        # Create a test customer
        self.customer = CustomUser.objects.create(email='testuser@example.com')

        self.order = Order.objects.create(
            delivery_option="takeaway",
            time_preferred=timezone.now(),
            customer=self.customer,
            restaurant=self.restaurant,
            total_price=50.00
        )

        # Create a test product
        self.product = Product.objects.create(name="Test Product", price=10.00, available_quantity=100,restaurant=self.restaurant)

        # Create a test OrderItem
        self.order_item = OrderItem.objects.create(
            order=self.order,
            item=self.product,
            quantity=3
        )

    def test_order_item_creation(self):
        """Test the creation of a new OrderItem instance."""
        self.assertIsInstance(self.order_item, OrderItem)
        self.assertEqual(OrderItem.objects.count(), 1)


    def test_order_item_quantity_default(self):
        """Test the default value of quantity in OrderItem."""
        order_item = OrderItem.objects.create(order=self.order, item=self.product)
        self.assertEqual(order_item.quantity, 1)


class DeliveryChargeModelTestCase(TestCase):
    def setUp(self):
        # Create a test order
        self.restaurant = Restaurant.objects.create(name='Test Restaurant', rate=3.0,location='123 Main St',road='address',city='city')

        # Create a test customer
        self.customer = CustomUser.objects.create(email='testuser@example.com')
        self.order = Order.objects.create(
            delivery_option="Pickup",
            time_preferred=timezone.now(),
            customer=self.customer,
            restaurant=self.restaurant,
            total_price=50.00
        )

        # Create a test DeliveryCharge
        self.delivery_charge = DeliveryCharge.objects.create(
            region="Test Region",
            charge=5.00,
            order=self.order
        )

    def test_delivery_charge_creation(self):
        """Test the creation of a new DeliveryCharge instance."""
        self.assertIsInstance(self.delivery_charge, DeliveryCharge)
        self.assertEqual(DeliveryCharge.objects.count(), 1)

