from rest_framework import serializers
from .models import Order, OrderItem, DeliveryCharge
class DeliveryChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCharge
        fields = ('id', 'region', 'charge')



class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields='__all__'
    def calculate_total_price(self,item_data):
        item_quantity = item_data['quantity']
        item_price=  item_data['item'].price
        order=Order.objects.get(id=item_data['order'].id)
        order.total_price+=(item_quantity*item_price)
        order.save()

    def create(self, validated_data):
        self.calculate_total_price(validated_data)
        return super().create(validated_data)
    
    def delete(self, instance):
        order = instance.order
        item_price = instance.item.price
        order.total_price -= (instance.quantity * item_price)
        order.save()
        instance.delete()

    def update(self, instance, validated_data):
        item_quantity = validated_data.get('quantity', instance.quantity)
        item_price = instance.item.price
        order = instance.order
        order.total_price -= (instance.quantity * item_price)  # Deduct the old item price
        order.total_price += (item_quantity * item_price)  # Add the updated item price
        order.save()

        instance.quantity = item_quantity
        instance.save()
        return instance
class OrderSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Order
        fields='__all__'


