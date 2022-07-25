from rest_framework import serializers

from mycv_django.apps.collaborations.serializers import CollaborationSerializer
from mycv_django.apps.projects.models import Project
from mycv_django.apps.technologies.models import ProjectTechnology


class ProjectTechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectTechnology
        fields = ('id', 'comment', 'name', 'content')
        depth = 1

    id = serializers.IntegerField(source='technology.id')
    name = serializers.CharField(source='technology.name')
    content = serializers.CharField(source='technology.content')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
        depth = 1

    collaborations = CollaborationSerializer(source='collaboration_set', many=True, read_only=True)
    technologies = ProjectTechnologySerializer(source='projecttechnology_set', many=True, read_only=True)


class ProjectDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

    collaborations = CollaborationSerializer(source='collaboration_set', many=True, read_only=True)
    technologies = ProjectTechnologySerializer(source='projecttechnology_set', many=True, read_only=True)
