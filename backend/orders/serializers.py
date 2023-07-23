from rest_framework import serializers

from products.models import Product
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Order
        fields='__all__'

class OrderwithItemsSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'delivery_option', 'customer',  'restaurant', 'total_price','time_preferred','order_items']
    def to_representation(self, instance):
        print(instance)
 
        return{
            'instance': OrderSerializer(instance).data,
            'order_items': OrderItemSerializer(OrderItem.objects.filter(order=instance),many=True).data

        }
    def calculate_total_price(self, order_items):
        total_price = 0
        for item_data in order_items:
            item_quantity = item_data['quantity']
            item_price=  item_data['item'].price
            total_price+=item_price *item_quantity
        return total_price
    
    def create(self, validated_data):
        order_items =validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for item_data in order_items:
            item_data['order'] = order
            order_item =  OrderItem.objects.create(**item_data)
        total=self.calculate_total_price(order_items)
        order.total_price=total
        order.save()
        return order

      

#     def update(self, instance, validated_data):
#         order_items_data = validated_data['order_items']
#         instance.delivery_option = validated_data.get('delivery_option', instance.delivery_option)
#         instance.time_preferred = validated_data.get('time_preferred', instance.time_preferred)
#         instance.total_price = validated_data.get('total_price', instance.total_price)
#         instance.save()

#         # Update order_items
#         order_item_ids = [item_data.get('id') for item_data in order_items_data if 'id' in item_data]
#         for item in instance.order_items.all():
#             if item.id not in order_item_ids:
#                 item.delete()

#         for item_data in order_items_data:
#             item_id = item_data.get('id')
#             if item_id:
#                 item = OrderItem.objects.get(id=item_id, order=instance)
#                 item.item = item_data.get('item', item.item)
#                 item.quantity = item_data.get('quantity', item.quantity)
#                 item.save()
#             else:
#                 OrderItem.objects.create(order=instance, **item_data)

#         return instance



from rest_framework import serializers
from .models import DeliveryCharge

class DeliveryChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCharge
        fields = ('id', 'region', 'charge')
