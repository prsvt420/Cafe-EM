from typing import Tuple

from django.db import models
from django.urls import reverse

from apps.dishes.models import Dish
from apps.orders.choices import OrderStatusChoices


class Order(models.Model):
    """Модель заказа"""

    table_number: models.PositiveSmallIntegerField = models.PositiveSmallIntegerField(
        verbose_name="Номер столика"
    )
    dishes: models.ManyToManyField = models.ManyToManyField(
        verbose_name="Блюда", to=Dish
    )
    total_price: models.DecimalField = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="Общая стоимость"
    )
    status: models.CharField = models.CharField(
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.PENDING,
        max_length=2,
        verbose_name="Статус",
    )

    class Meta:
        db_table: str = "orders"
        db_table_comment: str = "Таблица содержит список заказов"
        verbose_name: str = "Заказ"
        verbose_name_plural: str = "Заказы"
        ordering: Tuple = ("id",)

    def __str__(self) -> str:
        """
        Возвращает ID заказа

        Returns:
            str: ID заказа
        """
        return f"Заказ №{self.pk}"

    def get_absolute_update_url(self) -> str:
        """
        Возвращает абсолютный URL для обновления данного объекта

        Returns:
            str: Абсолютный URL для обновления данного объекта
        """
        return reverse("orders:order-update", kwargs={"pk": self.pk})

    def get_absolute_delete_url(self) -> str:
        """
        Возвращает абсолютный URL для удаления данного объекта

        Returns:
            str: Абсолютный URL для удаления данного объекта
        """
        return reverse("orders:order-delete", kwargs={"pk": self.pk})
