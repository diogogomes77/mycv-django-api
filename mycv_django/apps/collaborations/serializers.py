from rest_framework import serializers

from mycv_django.apps.collaborations.models import Collaboration


class CollaborationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Collaboration
        fields = '__all__'
