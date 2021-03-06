# Generated by Django 4.0.4 on 2022-04-30 15:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('technologies', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='collaborations',
            field=models.ManyToManyField(through='collaborations.Collaboration', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(through='technologies.ProjectTechnology', to='technologies.technology'),
        ),
    ]
