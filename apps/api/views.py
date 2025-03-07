from typing import Optional

from django.db.models import QuerySet
from rest_framework import viewsets

from ..dishes.models import Dish, TypeDish
from ..dishes.repositories import DishRepository, TypeDishRepository
from ..orders.models import Order
from ..orders.repositories import OrderRepository
from .filters import OrderFilter
from .serializers import DishSerializer, OrderSerializer, TypeDishSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """API для работы с заказами"""

    queryset: QuerySet[Order] = OrderRepository.get_orders()
    serializer_class: type = OrderSerializer
    filterset_class: type = OrderFilter

    def get_queryset(self, *args, **kwargs) -> QuerySet[Order]:
        """
        Возвращает список заказов

        Returns:
            QuerySet[Order]: Список заказов

        """
        query: Optional[str] = self.request.GET.get("q", "").strip().lower()

        if query:
            orders: QuerySet[Order] = OrderRepository().get_orders_by_search_query(
                query=query
            )

            if orders.exists():
                return orders

        return OrderRepository.get_orders()


class DishViewSet(viewsets.ModelViewSet):
    """API для работы с блюдами"""

    queryset: QuerySet[Dish] = DishRepository.get_dishes()
    serializer_class: type = DishSerializer


class TypeDishViewSet(viewsets.ModelViewSet):
    """API для работы с типами блюд"""

    queryset: QuerySet[TypeDish] = TypeDishRepository.get_types()
    serializer_class: type = TypeDishSerializer
