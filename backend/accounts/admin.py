from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser, Profile


class EmailUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password','email_confirmed')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(CustomUser, EmailUserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    # fields = ['user', 'bio', 'profile_image',  'phone_number']
    fields = ['user', 'bio', 'profile_image', 'date_of_birth', 'phone_number']

    # list_display = ['user', 'bio', 'profile_image', 'phone_number']
    list_display = ['user', 'bio', 'profile_image', 'date_of_birth', 'phone_number']

    # list_display = ['user', 'first_name', 'last_name', 'date_of_birth']v
    # Customize other options as needed
admin.site.register(Profile, ProfileAdmin)

# class cuserAdmin(admin.ModelAdmin):

#     list_display = ['user', 'email_confirmed']

# admin.site.register(CustomUser, cuserAdmin)