from rest_framework import permissions, viewsets

from mycv_django.apps.projects.models import Project
from mycv_django.apps.projects.serializers import (  # ProjectDetailSerializer,
    ProjectSerializer,
)


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint to handle project related requests.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"
