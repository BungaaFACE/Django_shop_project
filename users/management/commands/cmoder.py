from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='moder@gmail.com',
            first_name='moder',
            last_name='moder',
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )

        user.set_password('moder')
        user.groups.add(1)  # id группы модераторов
        user.save()
