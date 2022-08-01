# Generated by Django 4.0.4 on 2022-06-18 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technologies', '0001_initial'),
        ('collaborations', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaboration',
            name='technologies',
            field=models.ManyToManyField(related_name='collaborations', through='technologies.CollaborationTechnology', to='technologies.technology'),
        ),
    ]