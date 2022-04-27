from rest_framework import permissions, viewsets

from mycv_django.apps.businesses.models import Business
from mycv_django.apps.businesses.serializers import BusinessSerializer


class BusinessViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows businesses to be viewed or edited.
    """
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [permissions.IsAuthenticated]
