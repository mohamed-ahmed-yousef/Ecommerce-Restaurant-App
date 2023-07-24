from django.shortcuts import render

from rest_framework import viewsets,permissions

from products.models import Product
from .models import DeliveryCharge, Order, OrderItem
from .serializers import DeliveryChargeSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.response import Response
from rest_framework import status




class DeliveryChargeViewSet(viewsets.ModelViewSet):
    queryset = DeliveryCharge.objects.all()
    serializer_class = DeliveryChargeSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        else:
            return super().get_permissions()



class orderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderwithItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    def add_order(self,data,order):
        modify_items=[]
        for item_data in data:
            item_data['order']=order.id
            modify_items.append(item_data)
        return modify_items
    
    def create(self, request, *args, **kwargs):
        order = OrderSerializer(data=request.data)
        order.is_valid(raise_exception=True)
        order.save()
        order_items_data=self.add_order(request.data['order_items'],order.instance)
        order_items=OrderItemSerializer(data=order_items_data,many=True)
        order_items.is_valid(raise_exception=True)
        order_items.save()
        response_data = {
        'order':OrderSerializer(Order.objects.get(id=order.instance.id)).data,
        'order_items': order_items.data,
        }
        return Response(status=status.HTTP_201_CREATED, data=response_data)



