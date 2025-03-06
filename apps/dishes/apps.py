from django.apps import AppConfig


class DishesConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "apps.dishes"
    verbose_name: str = "Блюда"
    label: str = "dishes"
