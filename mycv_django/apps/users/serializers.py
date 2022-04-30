from rest_framework import serializers

from mycv_django.apps.users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_developer', 'is_manager')
