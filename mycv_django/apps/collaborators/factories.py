import factory
from faker import Faker

from . import models

fake = Faker()


class DeveloperFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory('mycv_django.apps.users.factories.UserFactory')

    class Meta:
        model = models.Developer


class ManagerFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory('mycv_django.apps.users.factories.UserFactory')

    class Meta:
        model = models.Manager
