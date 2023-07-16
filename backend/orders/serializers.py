from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    item_name = serializers.ReadOnlyField(source='item.name')

    class Meta:
        model = OrderItem
        fields = ['item', 'quantity', 'item_name']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    customer_name = serializers.ReadOnlyField(source='customer.name')

    class Meta:
        model = Order
        fields = ['id', 'delivery_option', 'customer', 'customer_name', 'restaurant', 'total_price', 'order_items']


from rest_framework import serializers
from .models import DeliveryCharge

class DeliveryChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCharge
        fields = ('id', 'region', 'charge')
