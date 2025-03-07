from django import forms

from apps.orders.choices import OrderStatusChoices
from apps.orders.models import Order


class OrderForm(forms.ModelForm):
    """Форма для работы с заказами"""

    class Meta:
        model: type = Order
        fields: tuple = ("table_number", "dishes", "status")

    status: forms.ChoiceField = forms.ChoiceField(
        choices=OrderStatusChoices.choices,
        initial=OrderStatusChoices.PENDING,
        required=False,
    )
