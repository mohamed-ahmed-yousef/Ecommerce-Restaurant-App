import uuid
from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Discount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=50)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.code
class Restaurant(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    house= models.CharField(max_length=100)
    road= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    delivery_time=  models.CharField(max_length=50)
    min_order= models.IntegerField(default=0)
    rate=models.DecimalField( max_digits=5 ,decimal_places=0)
    image = models.ImageField(upload_to='product_images/',null=True,blank=True)


    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True, null=True) 
    available_quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')


    

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    restaurant=models.ManyToManyField(Restaurant, blank=True )
    def __str__(self):
        return self.name
    