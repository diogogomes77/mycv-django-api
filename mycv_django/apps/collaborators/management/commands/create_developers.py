from mycv_django.apps.collaborators.factories import DeveloperFactory
from mycv_django.apps.common.management.base import CreateDataBaseCommand


class Command(CreateDataBaseCommand):

    help = 'Create few developers'

    def handle(self, *args, **options):
        super().handle(*args, **options)
        self.stdout.write(f'Creating {self.number} developers ...')
        DeveloperFactory.create_batch(size=self.number)
