from mycv_django.apps.businesses.factories import CountryFactory
from mycv_django.apps.common.management.base import CreateDataBaseCommand


class Command(CreateDataBaseCommand):

    help = 'Create few countries'

    def handle(self, *args, **options):
        super().handle(*args, **options)
        self.stdout.write(f'Creating {self.number} countries ...')
        CountryFactory.create_batch(size=self.number)
