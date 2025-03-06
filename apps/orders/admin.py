from typing import Tuple

from django.contrib import admin

from apps.orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Админка заказов"""

    fields: Tuple = (
        "table_number",
        "dishes",
        "status",
    )
    list_display: Tuple = ("table_number", "total_price", "status")
    list_filter: Tuple = ("status",)
    search_fields: Tuple = ("table_number", "status")
    list_per_page: int = 50
    list_editable: Tuple = ("status",)
