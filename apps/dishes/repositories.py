from django.db.models import QuerySet

from apps.dishes.models import Dish, TypeDish


class TypeDishRepository:
    """Репозиторий для работы с типами блюд"""

    @staticmethod
    def get_types() -> QuerySet[TypeDish]:
        """
        Возвращает все типы блюд из базы данных.
        """
        return TypeDish.objects.all()


class DishRepository:
    """Репозиторий для работы с блюдами"""

    @staticmethod
    def get_dishes() -> QuerySet[Dish]:
        """
        Возвращает все блюда из базы данных.
        """
        return Dish.objects.all().select_related("type")
