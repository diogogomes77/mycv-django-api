from rest_framework import serializers

from mycv_django.apps.collaborations.models import Collaboration
from mycv_django.apps.projects.models import Project
from mycv_django.apps.technologies.models import Technology


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


# class TechnologyParentCollaborationSerializer(TechnologyCollaborationSerializer):
#     class Meta(TechnologyCollaborationSerializer.Meta):
#         depth = 0


class TechnologyParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ("slug",)


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = "__all__"
        depth = 0
        lookup_field = "slug"

    # projects = serializers.ListField(source="projects_set")
    # collaborations = serializers.IntegerField()
    # parents = serializers.IntegerField()

    projects = TechnologyProjectSerializer(many=True)
    collaborations = TechnologyCollaborationSerializer(many=True)
    parents = TechnologyParentSerializer(many=True)
