from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'Create test data'

    def handle(self, *args, **options):
        management.call_command('create_developers', number=5)
        management.call_command('create_managers', number=5)
