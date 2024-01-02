from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='denis@denis.com',
            name='Denis',
            phone='+79876543210',
            is_staff=True,
            is_superuser=True,
            is_active=True

        )

        user.set_password('123456')
        user.save()