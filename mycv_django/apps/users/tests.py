from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.sites import AdminSite
from django.test import TestCase

from mycv_django.apps.users.admin import UserAdmin
from mycv_django.apps.users.models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testUser", email="testUser@email.com", password=""
        )
        self.user.set_password("secret")
        self.user.save()

    def test_user(self):
        self.assertEqual(self.user.email, "testUser@email.com")
        self.assertTrue(self.user.check_password("secret"))

    def test_is_developer(self):
        self.assertEqual(self.user.is_developer, False)

    def test_is_manager(self):
        self.assertEqual(self.user.is_manager, False)


class UserAdminTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username="testUser", email="testUser@email.com", password=""
        )
        cls.user.set_password("secret")
        cls.user.is_superuser = True
        cls.user.save()

    def setUp(self):
        self.site = AdminSite()

    def test_modeladmin_str(self):
        ma = ModelAdmin(User, self.site)
        self.assertEqual(str(ma), "users.ModelAdmin")

    def test_is_developer(self):
        user = User.objects.get(id=1)
        user_admin = UserAdmin(User, AdminSite)
        obj = user_admin.get_object(None, user.id)
        is_developer = user_admin.is_developer(obj)
        self.assertEquals(is_developer, False)

    def test_is_manager(self):
        user = User.objects.get(id=1)
        user_admin = UserAdmin(User, AdminSite)
        obj = user_admin.get_object(None, user.id)
        is_manager = user_admin.is_manager(obj)
        self.assertEquals(is_manager, False)
