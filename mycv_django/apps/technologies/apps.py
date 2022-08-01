from django.apps import AppConfig


class TechnologiesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mycv_django.apps.technologies"

    def ready(self):
        import mycv_django.apps.technologies.signals.handlers  # noqa: F401
