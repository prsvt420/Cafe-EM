from decimal import Decimal
from typing import Dict

from django.db.models import Q, QuerySet, Sum

from apps.orders.models import Order


class OrderRepository:
    @staticmethod
    def get_orders() -> QuerySet[Order]:
        """
        Возвращает список всех заказов

        Returns:
            QuerySet[Order]: Список всех заказов

        """
        return Order.objects.all().prefetch_related("dishes")

    def get_orders_by_search_query(self, query: str) -> QuerySet[Order]:
        """
        Возвращает список заказов по поисковому запросу


        Parameters:
            query: Optional[str] Поисковый запрос

        Returns:
            QuerySet[Order]: Список заказов

        """

        status_mapping: Dict = {"PG": "В ожидании", "RD": "Готово", "PD": "Оплачено"}

        filter_conditions: Q = Q(table_number__icontains=query)

        for short_status, display_status in status_mapping.items():

            if query in display_status.lower():
                filter_conditions |= Q(status=short_status)

        return self.get_orders().filter(filter_conditions).order_by("table_number")

    def get_paid_orders(self) -> QuerySet[Order]:
        """
        Возвращает список оплаченных заказов

        Returns:
            QuerySet[Order]: Список оплаченных заказов

        """
        return self.get_orders().filter(status="PD")

    def get_revenue(self) -> Decimal:
        """
        Возвращает выручку

        Returns:
            Decimal: Выручка

        """
        paid_orders: QuerySet[Order] = self.get_paid_orders()

        if paid_orders.exists():
            return paid_orders.aggregate(Sum("total_price"))["total_price__sum"]

        return Decimal(0)
