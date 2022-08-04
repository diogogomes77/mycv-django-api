from rest_framework import serializers

from mycv_django.apps.collaborations.models import Collaboration
from mycv_django.apps.projects.models import Project
from mycv_django.apps.technologies.models import Technology
from mycv_django.apps.users.serializers import UserSerializer


class TechnologyProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name", "slug")
        lookup_field = "slug"


class TechnologyCollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
        fields = ("id", "collaborator", "project")
        depth = 0

    collaborator = UserSerializer()
    project = TechnologyProjectSerializer()


class TechnologyParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ("slug",)


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = (
            "id",
            "projects",
            "collaborations",
            "parents",
            "name",
            "slug",
            "content",
        )
        depth = 0
        lookup_field = "slug"

    projects = TechnologyProjectSerializer(many=True)
    collaborations = TechnologyCollaborationSerializer(many=True)
    parents = TechnologyParentSerializer(many=True)
