# Generated by Django 4.0.4 on 2022-04-30 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('collaborations', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('content', models.TextField(blank=True, null=True)),
                ('parents', models.ManyToManyField(blank=True, related_name='children', through='technologies.ParentTechnology', to='technologies.technology')),
            ],
            options={
                'verbose_name_plural': 'technologies',
            },
        ),
        migrations.CreateModel(
            name='ProjectTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technologies.technology')),
            ],
        ),
        migrations.AddField(
            model_name='parenttechnology',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tech_parent', to='technologies.technology'),
        ),
        migrations.AddField(
            model_name='parenttechnology',
            name='technology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_tech', to='technologies.technology'),
        ),
        migrations.CreateModel(
            name='CollaborationTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('collaboration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collaborations.collaboration')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='technologies.technology')),
            ],
        ),
    ]
