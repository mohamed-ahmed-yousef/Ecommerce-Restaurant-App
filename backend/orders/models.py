from random import choices
from random import choices
import uuid
from django.db import models

from products.models import Product

# Create your models here.

delivery_choices = (
    ('delivery', 'delivery'),
    ('takeaway', 'takeaway'),
)

    
class Order(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    delivery_option = models.CharField(choices= delivery_choices ,max_length=50)
    time_preferred = models.DateTimeField()
    customer=models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    restaurant=models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=8, decimal_places=2,default="0")
    # order_items = models.ManyToManyField(OrderItem, related_name='order_items')
    def str__(self):
        return f"Order #{self.order_number} for {self.customer.name}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def str__(self):
        return f"{self.quantity} of {self.item.name}"

class DeliveryCharge(models.Model):
    region = models.CharField(max_length=255)
    charge = models.DecimalField(max_digits=6, decimal_places=2)
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.region} - Charge: {self.charge}"