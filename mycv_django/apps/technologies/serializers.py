from rest_framework import serializers

from mycv_django.apps.collaborations.models import Collaboration
from mycv_django.apps.projects.models import Project
from mycv_django.apps.technologies.models import Technology


class TechnologyProjectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name')


class TechnologyCollaborationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collaboration
        fields = ('id', 'collaborator', 'project')
        depth = 1


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'
        depth = 1

    projects = TechnologyProjectSerializer(many=True)
    collaborations = TechnologyCollaborationSerializer(many=True)
