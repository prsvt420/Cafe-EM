from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "apps.core"
    verbose_name: str = "Core"
    label: str = "core"
