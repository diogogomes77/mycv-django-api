from random import choice

import factory
from faker import Faker

from mycv_django.apps.collaborations.models import Collaboration
from mycv_django.apps.projects.models import Project

from . import models

fake = Faker()


def get_random_technology(technology=None):
    tech = technology.pk if technology else None
    # print('get_random_technology: ', tech)
    pks = models.Technology.objects.exclude(pk=tech).values_list('pk', flat=True)
    random_pk = choice(pks)
    random_object = models.Technology.objects.get(pk=random_pk)
    return random_object


class TechnologyFactory(factory.django.DjangoModelFactory):
    name = factory.LazyFunction(fake.job)
    content = factory.LazyFunction(lambda: fake.paragraph(nb_sentences=5))

    class Meta:
        model = models.Technology


class ParentTechnologyFactory(factory.django.DjangoModelFactory):
    technology = factory.LazyFunction(get_random_technology)
    parent = factory.LazyAttribute(lambda o: get_random_technology(o.technology))

    class Meta:
        model = models.ParentTechnology


def get_random_project():
    pks = Project.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_object = Project.objects.get(pk=random_pk)
    return random_object


class ProjectTechnologyFactory(factory.django.DjangoModelFactory):
    project = factory.LazyFunction(get_random_project)
    technology = factory.LazyFunction(get_random_technology)
    comment = factory.LazyFunction(lambda: fake.paragraph(nb_sentences=5))

    class Meta:
        model = models.ProjectTechnology


def get_random_collaboration():
    pks = Collaboration.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_object = Collaboration.objects.get(pk=random_pk)
    return random_object


class CollaborationTechnologyFactory(factory.django.DjangoModelFactory):
    collaboration = factory.LazyFunction(get_random_collaboration)
    technology = factory.LazyFunction(get_random_technology)
    comment = factory.LazyFunction(lambda: fake.paragraph(nb_sentences=5))

    class Meta:
        model = models.CollaborationTechnology
