from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='user@mail.com',
            first_name='User',
            last_name='Userov',
            is_superuser=False,
            is_staff=False,
            is_active=True,
        )

        user.set_password('my_p1')
        user.save()
