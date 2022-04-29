from mycv_django.apps.common.management.base import CreateDataBaseCommand
from mycv_django.apps.technologies.factories import ProjectTechnologyFactory


class Command(CreateDataBaseCommand):

    help = 'Create few project technologies'

    def handle(self, *args, **options):
        super().handle(*args, **options)
        self.stdout.write(f'Creating {self.number} project technologies ...')
        ProjectTechnologyFactory.create_batch(size=self.number)
