from typing import Dict, List, Optional

from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from apps.core.utils import request_is_ajax
from apps.orders.choices import OrderStatusChoices
from apps.orders.forms import OrderForm
from apps.orders.models import Order
from apps.orders.repositories import OrderRepository


class OrderCreateView(CreateView):
    """Страница создания заказа"""

    template_name: str = "orders/order_create.html"
    form_class: type = OrderForm
    success_url: str = reverse_lazy("orders:orders")
    model: type = Order


class OrdersListView(ListView):
    """Страница списка заказов"""

    model: type = Order
    template_name: str = "orders/orders.html"
    context_object_name: str = "orders"

    def get_context_data(self, *, object_list=None, **kwargs) -> Dict:
        """
        Возвращает словарь с данными для шаблона

        Returns:
            Dict: Словарь с данными для шаблона
        """
        context: Dict = super().get_context_data(**kwargs)

        if self.queryset:
            context["orders_revenue"] = OrderRepository().get_revenue()

        return context

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

        self.queryset = OrderRepository.get_orders()

        return self.queryset

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse | HttpResponse:
        """
        Обрабатывает GET-запрос
        """
        if request_is_ajax(request):
            orders: QuerySet[Order] = self.get_queryset()

            orders_json: List = [
                {
                    "id": order.id,
                    "table_number": order.table_number,
                    "dishes": [dish.name for dish in order.dishes.all()],
                    "total_price": order.total_price,
                    "status": order.status,
                    "status_display": order.get_status_display(),
                    "get_absolute_update_url": order.get_absolute_update_url(),
                }
                for order in orders
            ]

            return JsonResponse(orders_json, safe=False)

        return super().get(request, *args, **kwargs)


class OrderUpdateView(UpdateView):
    """Страница редактирования заказа"""

    template_name: str = "orders/order_update.html"
    model: type = Order
    form_class: type = OrderForm
    success_url: str = reverse_lazy("orders:orders")
    context_object_name: str = "order"

    def get_queryset(self) -> QuerySet[Order]:
        """
        Возвращает список заказов

        Returns:
            QuerySet[Order]: Список заказов

        """
        return OrderRepository.get_orders()

    def get_context_data(self, **kwargs) -> Dict:
        """
        Возвращает словарь с данными для шаблона

        Returns:
            Dict: Словарь с данными для шаблона
        """
        context = super().get_context_data(**kwargs)
        context["statuses"] = OrderStatusChoices.choices
        return context


class OrderDeleteView(DeleteView):
    """Страница удаления заказа"""

    template_name: str = "orders/order_delete.html"
    model: type = Order
    success_url: str = reverse_lazy("orders:orders")
    context_object_name: str = "order"
