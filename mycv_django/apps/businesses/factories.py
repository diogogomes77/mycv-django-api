from random import choice

import factory
from faker import Faker

from . import models

fake = Faker()


class CountryFactory(factory.django.DjangoModelFactory):
    country = factory.LazyFunction(fake.country)

    class Meta:
        model = models.Country


def get_random_country():
    pks = models.Country.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_object = models.Country.objects.get(pk=random_pk)
    return random_object


class BusinessFactory(factory.django.DjangoModelFactory):
    name = factory.LazyFunction(fake.company)
    country = factory.LazyFunction(get_random_country)

    class Meta:
        model = models.Business
