from rest_framework import serializers

from mycv_django.apps.technologies.models import Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'
        depth = 1
