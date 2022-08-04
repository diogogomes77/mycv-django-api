from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from mycv_django.apps.technologies.models import Technology


@receiver(pre_save, sender=Technology)
def technology_set_slug(sender, instance: Technology, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
