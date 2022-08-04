from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mycv_django.apps.projects"

    def ready(self):
        import mycv_django.apps.projects.signals.handlers  # noqa: F401
