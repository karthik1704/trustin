from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

from customers.models import Customer
from samples.models import Product, TestingParameter



@receiver(post_save, sender=Product)
def add_Product_id(sender, instance, created, **kwargs):
    if created:
        year = instance.created_at.strftime("%Y")
        prevyear = int(instance.created_at.strftime("%Y"))-1
        id = str(instance.id)
        product_code = f"SAM/{prevyear}-{year}/{id}"
        instance.product_code = product_code
        instance.save()

@receiver(post_save, sender=TestingParameter)
def add_parameter_id(sender, instance, created, **kwargs):
    if created:
        year = instance.created_at.strftime("%Y")
        prevyear = int(instance.created_at.strftime("%Y"))-1
        id = str(instance.id)
        parameter_code = f"TST/PARA/{prevyear}-{year}/{id}"
        instance.parameter_code = parameter_code
        instance.save()

    