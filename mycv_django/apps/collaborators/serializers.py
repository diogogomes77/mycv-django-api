from rest_framework import serializers

from mycv_django.apps.collaborators.models import Developer, Manager


class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Developer
        fields = ['user']


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ['user']
