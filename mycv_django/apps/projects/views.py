from rest_framework import permissions, viewsets
from rest_framework.response import Response

from mycv_django.apps.projects.models import Project
from mycv_django.apps.projects.serializers import (
    ProjectDetailSerializer,
    ProjectListSerializer,
)


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to handle project related requests.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProjectDetailSerializer(instance, context={'request': request})
        return Response(serializer.data)
