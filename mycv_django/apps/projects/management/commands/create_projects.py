from mycv_django.apps.common.management.base import CreateDataBaseCommand
from mycv_django.apps.projects.factories import ProjectFactory


class Command(CreateDataBaseCommand):

    help = 'Create few projects'

    def handle(self, *args, **options):
        super().handle(*args, **options)
        self.stdout.write(f'Creating {self.number} projects ...')
        ProjectFactory.create_batch(size=self.number)
