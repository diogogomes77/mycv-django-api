import datetime
from random import choice

import factory
from django.contrib.auth.models import Group
from faker import Faker

from mycv_django.apps.projects.models import Project
from mycv_django.apps.users.models import User

from . import models

fake = Faker()


def get_random_project():
    pks = Project.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_object = Project.objects.get(pk=random_pk)
    return random_object


def get_random_developer():
    pks = User.objects.filter(groups__name='developer').values_list('pk', flat=True)
    random_pk = choice(pks)
    random_object = User.objects.get(pk=random_pk)
    return random_object


def get_random_manager():
    pks = User.objects.filter(groups__name='manager').values_list('pk', flat=True)
    random_pk = choice(pks)
    random_object = User.objects.get(pk=random_pk)
    return random_object


def get_group_random_user(project):
    project_collaborators = project.collaborations.values_list('id', flat=True)
    groups_list = Group.objects.values_list('name', flat=True)
    group = choice(groups_list)
    pks = User.objects.filter(groups__name=group).exclude(pk__in=project_collaborators).values_list('pk', flat=True)
    try:
        random_pk = choice(pks)
        random_object = User.objects.get(pk=random_pk)
        return random_object
    except BaseException:
        return None


def get_random_date():
    start = fake.date_between_dates(
        date_start=datetime.datetime(2015, 1, 1),
        date_end=datetime.datetime(2021, 12, 31))
    start_b = start + datetime.timedelta(weeks=4)
    end = fake.date_between_dates(
        date_start=start_b,
        date_end=start_b + datetime.timedelta(weeks=56))
    return start, end


class CollaborationFactory(factory.django.DjangoModelFactory):
    project = factory.LazyFunction(get_random_project)
    collaborator = factory.LazyAttribute(lambda o: get_group_random_user(o.project))
    started_at = factory.LazyFunction(lambda: fake.date_between_dates(
        date_start=datetime.datetime(2015, 1, 1),
        date_end=datetime.datetime(2021, 12, 31)))
    ended_at = factory.LazyAttribute(lambda o: fake.date_between_dates(
        date_start=o.started_at + datetime.timedelta(weeks=4),
        date_end=o.started_at + datetime.timedelta(weeks=60)))

    class Meta:
        model = models.Collaboration
