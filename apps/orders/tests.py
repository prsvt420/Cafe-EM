from typing import Dict

from django.test import TestCase
from django.urls import reverse

from apps.dishes.models import Dish, TypeDish
from apps.orders.models import Order


class OrderCreateViewTests(TestCase):
    """Тестирование создания заказа"""

    def setUp(self) -> None:
        """Инициализация тестов"""
        self.url = reverse("orders:order-create")
        type_dish: TypeDish = TypeDish.objects.create(name="Тестовый тип блюда")
        self.dish = Dish.objects.create(
            name="Тестовое блюдо", type=type_dish, description="Описание", price=50.00
        )

    def test_create_order(self) -> None:
        """Проверка успешного создания заказа"""
        data: Dict = {
            "table_number": 1,
            "dishes": [self.dish.id],  # Используем созданное тестовое блюдо
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Order.objects.filter(table_number=1).exists())

        order: Order = Order.objects.get(table_number=1)

        self.assertEqual(order.total_price, 50.00)
        self.assertEqual(order.status, "PG")


class OrdersListViewTests(TestCase):
    """Тестирование отображения списка заказов"""

    def setUp(self) -> None:
        """Инициализация тестов"""
        self.url: str = reverse("orders:orders")

        self.dish_1 = Dish.objects.create(
            name="Тестовое блюдо 1",
            type=TypeDish.objects.create(name="Тестовый тип блюда 1"),
            description="Описание",
            price=50.00,
        )

        self.dish_2 = Dish.objects.create(
            name="Тестовое блюдо 2",
            type=TypeDish.objects.create(name="Тестовый тип блюда 2"),
            description="Описание",
            price=100.00,
        )

        self.order_1: Order = Order.objects.create(table_number=1)
        self.order_1.dishes.set([self.dish_1, self.dish_2])
        self.order_2: Order = Order.objects.create(table_number=2)
        self.order_2.dishes.set([self.dish_1])

    def test_orders_list_view(self) -> None:
        """Проверка успешного отображения списка заказов"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "orders/orders.html")
        self.assertEqual(len(response.context["orders"]), 2)

    def test_orders_revenue_in_context(self) -> None:
        """Проверка, что выручка отображается в контексте"""
        response = self.client.get(self.url)
        self.assertIn("orders_revenue", response.context)

        self.assertEqual(response.context["orders_revenue"], 0)

        self.order_1.status = "PD"
        self.order_1.save()

        response = self.client.get(self.url)
        self.assertEqual(response.context["orders_revenue"], 150.00)

    def test_orders_list_view_with_search(self) -> None:
        """Проверка фильтрации заказов по поисковому запросу"""
        response = self.client.get(self.url, {"q": "1"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["orders"]), 1)
        self.assertEqual(response.context["orders"][0], self.order_1)


class OrderUpdateViewTests(TestCase):
    """Тестирование обновления заказа"""

    def setUp(self) -> None:

        self.dish = Dish.objects.create(
            name="Тестовое блюдо",
            type=TypeDish.objects.create(name="Тестовый тип блюда"),
            description="Описание",
            price=50.00,
        )

        self.order: Order = Order.objects.create(table_number=1)
        self.order.dishes.set([self.dish])

        self.url: str = self.order.get_absolute_update_url()

    def test_update_order(self) -> None:
        """Проверка успешного обновления заказа"""
        data = {
            "table_number": 2,
            "dishes": [self.dish.id],
        }
        response = self.client.post(self.url, data)
        self.order.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.order.table_number, 2)


class OrderDeleteViewTests(TestCase):
    """Тестирование удаления заказа"""

    def setUp(self) -> None:
        """Инициализация тестов"""

        self.dish: Dish = Dish.objects.create(
            name="Тестовое блюдо",
            type=TypeDish.objects.create(name="Тестовый тип блюда"),
            description="Описание",
            price=50.00,
        )

        self.order: Order = Order.objects.create(table_number=1)
        self.order.dishes.set([self.dish])

        self.url: str = self.order.get_absolute_delete_url()

    def test_delete_order(self) -> None:
        """Проверка успешного удаления заказа"""
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Order.objects.filter(pk=self.order.pk).exists())
