from django.test import TestCase

from mycv_django.apps.collaborators.models import Developer, Manager
from mycv_django.apps.users.models import User


class DeveloperModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="testUser", email="testUser@email.com", password=""
        )
        user.set_password("secret")
        user.save()
        self.developer = Developer.objects.create(
            user=user
        )

    def test_is_developer(self):
        self.assertEqual(self.developer.user.is_developer, True)


class ManagerModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(
            username="testUser", email="testUser@email.com", password=""
        )
        user.set_password("secret")
        user.save()
        self.manager = Manager.objects.create(
            user=user
        )

    def test_is_developer(self):
        self.assertEqual(self.manager.user.is_manager, True)
