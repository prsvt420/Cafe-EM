from django.db.models import QuerySet

from apps.dishes.models import Dish


class DishRepository:
    @staticmethod
    def get_dishes() -> QuerySet[Dish]:
        """
        Возвращает все блюда из базы данных.
        """
        return Dish.objects.all().select_related("type")
