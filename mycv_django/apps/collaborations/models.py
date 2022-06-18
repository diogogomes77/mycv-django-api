from django.db import models

from mycv_django.apps.technologies.models import (
    CollaborationTechnology,
    Technology,
)


class Collaboration(models.Model):
    project = models.ForeignKey('projects.Project',
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)

    collaborator = models.ForeignKey('users.User',
                                     limit_choices_to={'groups__name__in': ['developer', 'manager']},
                                     null=False,
                                     blank=False,
                                     on_delete=models.CASCADE)

    started_at = models.DateField(null=True, blank=True)
    ended_at = models.DateField(null=True, blank=True)

    technologies = models.ManyToManyField(Technology,
                                          related_name='collaborations',
                                          through=CollaborationTechnology,
                                          through_fields=['collaboration', 'technology'])

    @property
    def id(self):
        return self.id

    def __str__(self) -> str:
        return f"{self.collaborator} on {self.project}"
