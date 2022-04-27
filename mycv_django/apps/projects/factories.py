from random import choice

import factory
from faker import Faker

from mycv_django.apps.businesses.models import Business

from . import models

fake = Faker()


def get_random_business():
    pks = Business.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_object = Business.objects.get(pk=random_pk)
    return random_object


class ProjectFactory(factory.django.DjangoModelFactory):
    name = factory.LazyFunction(fake.job)
    description = factory.LazyFunction(lambda: fake.paragraph(nb_sentences=5))
    business = factory.LazyFunction(get_random_business)

    class Meta:
        model = models.Project
