from typing import List

from django.urls import path

from . import views

app_name: str = "orders"

urlpatterns: List = [
    path(
        "create/",
        views.OrderCreateView.as_view(),
        name="order-create",
    ),
    path("", views.OrdersListView.as_view(), name="orders"),
    path("<int:pk>/update/", views.OrderUpdateView.as_view(), name="order-update"),
    path("<int:pk>/delete/", views.OrderDeleteView.as_view(), name="order-delete"),
]
