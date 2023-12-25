from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

from customers.models import Customer



@receiver(post_save, sender=Customer)
def add_customer_id(sender, instance, created, **kwargs):
    if created:
        year = instance.created_at.strftime("%Y")
        prevyear = int(instance.created_at.strftime("%Y"))-1
        id = str(instance.id)
        customer_code = f"CUS/{prevyear}-{year}/{id}"
        instance.customer_code = customer_code
        instance.save()

    