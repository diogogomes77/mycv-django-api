from rest_framework import serializers

from mycv_django.apps.collaborations.models import Collaboration
from mycv_django.apps.projects.models import Project
from mycv_django.apps.technologies.models import CollaborationTechnology
from mycv_django.apps.users.serializers import UserSerializer


class CollaborationTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = CollaborationTechnology
        fields = (
            "technology_id",
            "technology_slug",
            "comment",
            "technology_name",
            "technology_content",
        )
        depth = 0

    technology_id = serializers.IntegerField(source="technology.id")
    technology_slug = serializers.CharField(source="technology.slug")
    technology_name = serializers.CharField(source="technology.name")
    technology_content = serializers.CharField(source="technology.content")


class CollaborationProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "slug", "name")


class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
        depth = 0
        fields = (
            "id",
            "collaborator",
            "started_at",
            "ended_at",
            "collaboration_technologies",
            "project",
        )

    collaborator = UserSerializer()
    collaboration_technologies = CollaborationTechnologySerializer(
        source="collaborationtechnology_set", many=True, read_only=True
    )

    project = CollaborationProjectSerializer()
