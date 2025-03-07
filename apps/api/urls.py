from typing import List

from django.urls import include, path
from rest_framework import routers

from . import views
from .yasg import urlpatterns as yasg_urls

app_name: str = "api"

router: routers.DefaultRouter = routers.DefaultRouter()

router.register("orders", views.OrderViewSet, basename="orders")
router.register("type_dishes", views.TypeDishViewSet, basename="type_dishes")
router.register("dishes", views.DishViewSet, basename="dishes")

urlpatterns: List = [
    path("", include(router.urls)),
]

urlpatterns += yasg_urls
