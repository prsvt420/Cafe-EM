from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "apps.orders"
    verbose_name: str = "Заказы"
    label: str = "orders"

    def ready(self) -> None:
        import apps.orders.signals  # noqa
