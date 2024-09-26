from django.contrib import admin

from .models import Campaign, Restaurant

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Campaign)

