import factory
from faker import Faker

from . import models

fake = Faker()


class ProjectFactory(factory.django.DjangoModelFactory):
    name = factory.LazyFunction(fake.job)
    description = factory.LazyFunction(lambda: fake.paragraph(nb_sentences=5))

    class Meta:
        model = models.Project
