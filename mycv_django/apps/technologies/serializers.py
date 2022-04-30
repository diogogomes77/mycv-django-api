from rest_framework import serializers

from mycv_django.apps.technologies.models import Technology


class TechnologySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'
