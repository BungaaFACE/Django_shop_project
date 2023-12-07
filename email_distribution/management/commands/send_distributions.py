from django.core.management import BaseCommand
from email_distribution.services import start_distribution_task


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        start_distribution_task()
