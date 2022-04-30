from mycv_django.apps.common.management.base import CreateDataBaseCommand
from mycv_django.apps.technologies.factories import (
    ParentTechnologyFactory,
    TechnologyFactory,
)


class Command(CreateDataBaseCommand):

    help = 'Create few technologies'

    def handle(self, *args, **options):
        super().handle(*args, **options)
        self.stdout.write(f'Creating {self.number} technologies ...')
        TechnologyFactory.create_batch(size=self.number)
        self.stdout.write(f'Creating {self.number} parent technologies ...')
        ParentTechnologyFactory.create_batch(size=self.number)
