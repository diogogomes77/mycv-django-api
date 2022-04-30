from mycv_django.apps.collaborations.factories import CollaborationFactory
from mycv_django.apps.common.management.base import CreateDataBaseCommand


class Command(CreateDataBaseCommand):

    help = 'Create few collaborations'

    def handle(self, *args, **options):
        super().handle(*args, **options)
        self.stdout.write(f'Creating {self.number} collaborations ...')
        CollaborationFactory.create_batch(size=self.number)
