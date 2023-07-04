from django.conf import settings
from django.db import models


from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _
from PIL import Image
class CustomUserManager(BaseUserManager):


    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    email_confirmed = models.BooleanField(_('email confirmed'), default=False)
    profile_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email
    
class Profile(models.Model):
        user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True,default='')
        
        bio = models.TextField(blank=True)
        profile_image = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
        date_of_birth = models.DateField(null=True, blank=True)
        phone_number = models.CharField(max_length=20, null=True, blank=True)

        def __str__(self):
            return self.user.first_name