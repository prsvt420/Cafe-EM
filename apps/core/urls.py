from typing import List

from django.urls import path

from . import views

app_name: str = "core"

urlpatterns: List = [
    path("", views.redirect_to_orders, name="redirect_to_orders"),
]
