from django import template
from django.db.models import QuerySet

from apps.dishes.models import Dish
from apps.dishes.repositories import DishRepository

register: template.Library = template.Library()


@register.simple_tag
def get_all_dishes() -> QuerySet[Dish]:
    """
    Возвращает все блюда из базы данных.
    """
    return DishRepository.get_dishes()
