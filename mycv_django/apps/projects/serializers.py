from rest_framework import serializers

from mycv_django.apps.collaborations.serializers import CollaborationSerializer
from mycv_django.apps.projects.models import Project
from mycv_django.apps.technologies.models import ProjectTechnology


class ProjectTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTechnology
        fields = (
            "technology_id",
            "technology_slug",
            "comment",
            "technology_name",
            "technology_content",
            # "technology",
        )
        depth = 0

    technology_id = serializers.IntegerField(source="technology.id")
    technology_slug = serializers.CharField(source="technology.slug")
    technology_name = serializers.CharField(source="technology.name")
    technology_content = serializers.CharField(source="technology.content")


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        depth = 0
        lookup_field = "slug"

    collaborations = CollaborationSerializer(
        source="collaboration_set", many=True, read_only=True
    )
    project_technologies = ProjectTechnologySerializer(
        source="projecttechnology_set", many=True, read_only=True
    )
