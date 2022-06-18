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

    def __str__(self) -> str:
        return f"{self.get_full_name()} ({self.roles})"

    @property
    def roles(self):
        roles = []
        if self.is_manager:
            roles.append("manager")
        if self.is_developer:
            roles.append("developer")

        return ", ".join(roles)
