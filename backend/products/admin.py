from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ProductImage, category, Discount, Product

admin.site.register(category)
admin.site.register(Discount)
admin.site.register(Product)
admin.site.register(ProductImage)