from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    @property
    def is_developer(self) -> bool:
        """Define if the user is related to a developer."""
        return hasattr(self, 'developer')

    @property
    def is_manager(self) -> bool:
        """Define if the user is related to a manager."""
        return hasattr(self, 'manager')
