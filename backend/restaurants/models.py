import uuid
from django.db import models

# Create your models here.
class Restaurant(models.Model):
    # id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    
class Campaign(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    restaurant=models.ManyToManyField(Restaurant, blank=True )
    def __str__(self):
        return self.name
    