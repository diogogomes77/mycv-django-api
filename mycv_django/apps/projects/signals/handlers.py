from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from mycv_django.apps.projects.models import Project


@receiver(pre_save, sender=Project)
def project_set_slug(sender, instance: Project, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
