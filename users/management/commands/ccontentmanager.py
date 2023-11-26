from django.core.management import BaseCommand
from users.models import User
from django.contrib.auth.models import Group


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
        group = Group.objects.get(name='Контент-менеджер')
        group.user_set.add(user)
        # user.groups.add(2)
        user.save()
