from rest_framework import serializers

from mycv_django.apps.businesses.models import Business


class BusinessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'
