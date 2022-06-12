from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from mycv_django.apps.projects.models import Project
from mycv_django.apps.projects.serializers import (
    ProjectDetailSerializer,
    ProjectListSerializer,
)


class ProjectViewSet(viewsets.ViewSet):
    """
    ViewSet for listing or retrieving projects.
    """

    def list(self, request):
        queryset = Project.objects.all()
        serializer = ProjectListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Project.objects.all()
        project = get_object_or_404(queryset, pk=pk)
        serializer = ProjectDetailSerializer(project, context={'request': request})
        return Response(serializer.data)
