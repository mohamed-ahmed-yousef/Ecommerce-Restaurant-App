from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Campaign, ProductImage, Restaurant, Category, Discount, Product

admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Restaurant)
admin.site.register(Campaign)