from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Resets the database and applies all migrations.'

    def handle(self, *args, **options):
        # Step 1: Reset the database
        self.stdout.write(self.style.WARNING("Resetting the database..."))
        call_command('flush', interactive=False, verbosity=0)
        
        # Step 2: Apply migrations
        self.stdout.write(self.style.WARNING("Applying migrations..."))
        call_command('migrate', verbosity=0)

        self.stdout.write(self.style.SUCCESS("Database reset and migrations applied successfully."))
c=Command()
c.handle()