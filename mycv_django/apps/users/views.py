from rest_framework import viewsets

from mycv_django.apps.users.models import User
from mycv_django.apps.users.serializers import UserSerializer


class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
