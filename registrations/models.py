from django.db import models

from trf.models import TRF

# Create your models here.
class Registraion(models.Model):
    trf = models.ForeignKey(TRF, related_name='registration_trf', on_delete=models.CASCADE)