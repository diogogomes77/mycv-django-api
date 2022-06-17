from rest_framework import serializers

from mycv_django.apps.collaborations.models import Collaboration


class CollaborationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collaboration
        depth = 2
        fields = ('id', 'collaborator', 'started_at', 'ended_at', 'technologies')
