from rest_framework import permissions, viewsets

from mycv_django.apps.collaborators.models import Developer, Manager
from mycv_django.apps.collaborators.serializers import (
    DeveloperSerializer,
    ManagerSerializer,
)


class DeveloperViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows developers to be viewed or edited.
    """
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ManagerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows managers to be viewed or edited.
    """
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
