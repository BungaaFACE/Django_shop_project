from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='content@gmail.com',
            first_name='content',
            last_name='content',
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )

        user.set_password('content')
        user.groups.add(2)
        user.save()
