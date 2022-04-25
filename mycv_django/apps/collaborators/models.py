from django.db import models


class Developer(models.Model):
    user = models.OneToOneField('users.User', related_name='developer', on_delete=models.CASCADE)


class Manager(models.Model):
    user = models.OneToOneField('users.User', related_name='manager', on_delete=models.CASCADE)
