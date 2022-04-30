from rest_framework import permissions, viewsets

from mycv_django.apps.collaborations.models import Collaboration
from mycv_django.apps.collaborations.serializers import CollaborationSerializer


class CollaborationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows collaborations to be viewed or edited.
    """
    queryset = Collaboration.objects.all()
    serializer_class = CollaborationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
