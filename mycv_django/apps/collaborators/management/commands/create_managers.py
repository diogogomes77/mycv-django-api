from mycv_django.apps.collaborators.factories import ManagerFactory
from mycv_django.apps.common.management.base import CreateDataBaseCommand


class Command(CreateDataBaseCommand):

    help = 'Create few managers'

    def handle(self, *args, **options):
        super().handle(*args, **options)
        self.stdout.write(f'Creating {self.number} managers ...')
        ManagerFactory.create_batch(size=self.number)
