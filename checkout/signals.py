from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import ToPayLineItem

@receiver(post_save, sender=ToPayLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    handles signals from post save event
    sender of the signal - update or create order line item
    """
    instance.order.update_total()


@receiver(post_delete, sender=ToPayLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()