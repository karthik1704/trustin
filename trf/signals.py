from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

from trf.models import TRF


@receiver(post_save, sender=TRF)
def add_trf_id(sender, instance, created, **kwargs):
    if created:
        year = instance.created_at.strftime("%Y")
        prevyear = int(instance.created_at.strftime("%Y"))-1
        id = str(instance.id)
        trf_code = f"TRF-{prevyear}-{year}-{id}"
        instance.trf_code = trf_code
        instance.save()

    