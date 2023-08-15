from user.models import CustomUser
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        email = 'vitoradmin@admin.com'
        password = 'admin'

        if not CustomUser.objects.filter(email=email).exists():
            CustomUser.objects.create_superuser(email=email, password=password)

            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))