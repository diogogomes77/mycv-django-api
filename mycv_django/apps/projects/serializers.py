from rest_framework import serializers

from mycv_django.apps.collaborations.serializers import CollaborationSerializer
from mycv_django.apps.projects.models import Project
from mycv_django.apps.technologies.models import ProjectTechnology


class ProjectListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'description')


class ProjectTechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectTechnology
        fields = ('id', 'technology', 'comment')
        depth = 1


class ProjectDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

    collaborations = CollaborationSerializer(source='collaboration_set', many=True, read_only=True)
    technologies = ProjectTechnologySerializer(source='projecttechnology_set', many=True, read_only=True)
