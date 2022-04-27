from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=64, blank=False)
    description = models.TextField(blank=True)
    collaborations = models.ManyToManyField('users.User',
                                            through='collaborations.Collaboration',
                                            through_fields=['project', 'collaborator'])

    def __str__(self):
        return self.name
