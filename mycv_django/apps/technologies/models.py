from django.db import models


class Technology(models.Model):
    class Meta:
        verbose_name_plural = "technologies"

    name = models.CharField(max_length=64, blank=False)
    content = models.TextField(null=True, blank=True)
    parents = models.ManyToManyField(
        'self', blank=True,
        through='ParentTechnology',
        through_fields=["technology", "parent"],
        related_name="children",
        symmetrical=False
    )

    def __str__(self):
        return self.name

    @property
    def id(self):
        return self.id


class ParentTechnology(models.Model):
    technology = models.ForeignKey(
        Technology,
        on_delete=models.CASCADE,
        related_name='parent_tech'
    )
    parent = models.ForeignKey(
        Technology,
        on_delete=models.CASCADE,
        related_name='tech_parent'
    )

    @property
    def id(self):
        return self.id


class ProjectTechnology(models.Model):
    project = models.ForeignKey('projects.Project',
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    technology = models.ForeignKey(
        Technology,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    comment = models.TextField(null=True, blank=True)

    @property
    def id(self):
        return self.id


class CollaborationTechnology(models.Model):
    collaboration = models.ForeignKey('collaborations.Collaboration',
                                      null=False,
                                      blank=False,
                                      on_delete=models.CASCADE)
    technology = models.ForeignKey(
        Technology,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    comment = models.TextField(null=True, blank=True)
