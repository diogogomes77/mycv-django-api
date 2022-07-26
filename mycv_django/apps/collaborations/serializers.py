from django.contrib.auth.models import Group
from rest_framework import serializers

from mycv_django.apps.collaborations.models import Collaboration


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "name")


class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
        depth = 1
        fields = (
            "id",
            "groups",
            "collaborator",
            "started_at",
            "ended_at",
            "technologies",
        )

    groups = GroupSerializer(many=True, source="collaborator.groups")
