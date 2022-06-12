from rest_framework import serializers

from mycv_django.apps.collaborations.serializers import CollaborationSerializer
from mycv_django.apps.projects.models import Project


class ProjectListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'description')


class ProjectDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

    collaborations = CollaborationSerializer(source='collaboration_set', many=True, read_only=True)


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
