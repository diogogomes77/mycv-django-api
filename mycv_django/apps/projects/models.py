from django.db import models

from mycv_django.apps.technologies.models import ProjectTechnology, Technology


class Project(models.Model):
    name = models.CharField(max_length=64, blank=False)
    description = models.TextField(blank=True)
    collaborations = models.ManyToManyField('users.User',
                                            through='collaborations.Collaboration',
                                            through_fields=['project', 'collaborator'])
    business = models.ForeignKey('businesses.Business',
                                 related_name='projects',
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE)
    technologies = models.ManyToManyField(Technology,
                                          through=ProjectTechnology,
                                          through_fields=['project', 'technology'])

    def __str__(self):
        return self.name

    @property
    def id(self):
        return self.id
