from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создание обычного поьзователя"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email='no@rights.com',
            name='Denis',
            phone='+79876543210',
            is_staff=True,
            is_superuser=False,
            is_active=True

        )

        user.set_password('123456')
        user.save()
