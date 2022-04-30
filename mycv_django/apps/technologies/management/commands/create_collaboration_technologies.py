from mycv_django.apps.common.management.base import CreateDataBaseCommand
from mycv_django.apps.technologies.factories import (
    CollaborationTechnologyFactory,
)


class Command(CreateDataBaseCommand):

    help = 'Create few collaboration technologies'

    def handle(self, *args, **options):
        super().handle(*args, **options)
        self.stdout.write(f'Creating {self.number} collaboration technologies ...')
        CollaborationTechnologyFactory.create_batch(size=self.number)
