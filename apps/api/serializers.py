from typing import List

from rest_framework import serializers

from apps.dishes.models import Dish, TypeDish
from apps.orders.models import Order


class TypeDishSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с типами блюд"""

    class Meta:
        model: type = TypeDish
        fields: str = "__all__"


class DishSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с блюдами"""

    class Meta:
        model: type = Dish
        fields: str = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с заказами"""

    status: serializers.CharField = serializers.CharField(
        source="get_status_display", read_only=True
    )

    class Meta:
        model: type = Order
        fields: str = "__all__"
        read_only_fields: List[str] = ["total_price"]
