from typing import Tuple

from django.contrib import admin

from apps.dishes.models import Dish, TypeDish


@admin.register(TypeDish)
class TypeDishAdmin(admin.ModelAdmin):
    """Админка типов блюд"""

    list_display: Tuple = ("name",)
    list_per_page: int = 25


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    """Админка блюд"""

    list_display: Tuple = ("name", "price", "type")
    list_filter: Tuple = ("type",)
    search_fields: Tuple = ("name",)
    list_per_page: int = 50
