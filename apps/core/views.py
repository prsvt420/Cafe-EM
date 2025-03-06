from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect


def redirect_to_orders(request: HttpRequest) -> HttpResponseRedirect:
    """
    Перенаправляет пользователя на страницу с заказами.

    Returns:
        HttpResponseRedirect: Страница с заказами
    """
    return redirect("orders:orders")
