from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderStatusChoices(models.TextChoices):
    """Статусы заказа"""

    PENDING = "PG", _("В ожидании")
    READY = "RD", _("Готово")
    PAID = "PD", _("Оплачено")
