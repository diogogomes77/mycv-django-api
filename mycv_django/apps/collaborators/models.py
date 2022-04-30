from django.contrib.auth.models import Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Developer(models.Model):
    user = models.OneToOneField('users.User', related_name='developer', on_delete=models.CASCADE)


class Manager(models.Model):
    user = models.OneToOneField('users.User', related_name='manager', on_delete=models.CASCADE)


@receiver(post_save, sender=Developer)
def add_user_to_group_developer(sender, instance, created: bool, **kwargs):
    if created:
        group, group_created = Group.objects.get_or_create(name='developer')
        instance.user.groups.add(group)
        instance.user.save()


@receiver(post_save, sender=Manager)
def add_user_to_group_manager(sender, instance, created: bool, **kwargs):
    if created:
        group, group_created = Group.objects.get_or_create(name='manager')
        instance.user.groups.add(group)
        instance.user.save()
