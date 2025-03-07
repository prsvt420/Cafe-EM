from typing import List

from django_filters import rest_framework as filters

from apps.orders.models import Order


class OrderFilter(filters.FilterSet):
    """Фильтр заказов"""

    class Meta:
        model: type = Order
        fields: List = ["status"]
