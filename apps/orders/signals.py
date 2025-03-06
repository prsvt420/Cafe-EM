from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from apps.orders.models import Order


@receiver(m2m_changed, sender=Order.dishes.through)
def update_order_total_price(
    sender: Order, instance: Order, action: str, **kwargs
) -> None:
    """Обновляет общую стоимость заказа при изменении списка блюд в заказе"""
    if action in ["post_add", "post_remove", "post_clear"]:
        instance.total_price = sum(dish.price for dish in instance.dishes.all())
        instance.save(update_fields=["total_price"])
