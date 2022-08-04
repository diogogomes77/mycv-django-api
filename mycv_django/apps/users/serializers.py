from rest_framework import serializers

from mycv_django.apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("full_name", "username", "email", "is_developer", "is_manager")

    def get_full_name(self, obj):
        return obj.get_full_name()
