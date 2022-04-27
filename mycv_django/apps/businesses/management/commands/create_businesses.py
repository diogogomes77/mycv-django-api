from mycv_django.apps.businesses.factories import BusinessFactory
from mycv_django.apps.common.management.base import CreateDataBaseCommand


class Command(CreateDataBaseCommand):

    help = 'Create few businesses'

    def handle(self, *args, **options):
        super().handle(*args, **options)
        self.stdout.write(f'Creating {self.number} businesses ...')
        BusinessFactory.create_batch(size=self.number)
