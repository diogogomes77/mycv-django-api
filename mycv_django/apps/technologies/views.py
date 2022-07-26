from rest_framework import permissions, viewsets

from mycv_django.apps.technologies.models import Technology
from mycv_django.apps.technologies.serializers import TechnologySerializer


class TechnologyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows technologies to be viewed or edited.
    """

    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
