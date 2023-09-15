import os
from user.models import CustomUser
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        if not CustomUser.objects.filter(email=email).exists():
            CustomUser.objects.create_superuser(email=email, username=username, password=password)

            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))