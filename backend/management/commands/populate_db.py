import os
from django.core.management.base import BaseCommand
import django

from faker import Faker


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'accounts.settings') # this should be done first.
django.setup() #

from accounts.models import CustomUser

class Command(BaseCommand):
    help = 'Populates the database with random data.'

    def handle(self, *args, **options):
        fake = Faker()

        # Create some sample users
        for _ in range(10):
            CustomUser.objects.create_user(
                name=fake.user_name(),
                email=fake.email(),
                password='password'  # You can change this if you prefer random passwords
            )

        # Add more code here to create other random data for your models as needed

        self.stdout.write(self.style.SUCCESS("Database successfully populated with random data."))

