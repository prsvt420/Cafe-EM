from typing import Tuple

from django.db import models


class TypeDish(models.Model):
    """Модель типа блюда"""

    name: models.CharField = models.CharField(
        verbose_name="Название", max_length=100, unique=True
    )

    class Meta:
        db_table: str = "types"
        db_table_comment: str = "Таблица содержит список типов блюд"
        verbose_name: str = "Тип блюда"
        verbose_name_plural: str = "Типы блюд"
        ordering: Tuple = ("id",)

    def __str__(self) -> str:
        """
        Возвращает название типа блюда

        Returns:
            str: Название типа блюда
        """
        return self.name


class Dish(models.Model):
    """Модель блюда"""

    name: models.CharField = models.CharField(
        verbose_name="Название", max_length=100, unique=True
    )
    description: models.TextField = models.TextField(verbose_name="Описание")
    price: models.DecimalField = models.DecimalField(
        verbose_name="Цена", max_digits=7, decimal_places=2
    )
    type: models.ForeignKey = models.ForeignKey(
        verbose_name="Тип блюда", to=TypeDish, on_delete=models.CASCADE
    )

    class Meta:
        db_table: str = "dishes"
        db_table_comment: str = "Таблица содержит список блюд"
        verbose_name: str = "Блюдо"
        verbose_name_plural: str = "Блюда"
        ordering: Tuple = ("id",)

    def __str__(self) -> str:
        """
        Возвращает название блюда

        Returns:
            str: Название блюда
        """
        return self.name
