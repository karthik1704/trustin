from django.db import models
from django.utils import timezone
from accounts.models import Hod
import registrations
from samples.models import TestType
from trf.models import TRF

NABL = (
    ("YES", "Yes"),
    ("PARTIAL", "Partial"),
    ("NO", "No"),
    ("NA", "NA"),
)
CDSCO = (
    ("YES", "Yes"),
    ("NO", "No"),
    ("NA", "NA"),
)
SAMPLE_CONDITION = (
    ("GOOD", "Good"),
    ("BAD", "Bad"),
)
SAMPLE_QUANTITY = (
    ("SUFFICIENT", "Sufficient"),
    ("NEED_MORE", "Need More"),
)
MODE_OF_RECEIVED = (
    ("COURIER", "Courier"),
    ("INPERSON", "Inperson"),
)



# Create your models here.
class Registration(models.Model):
    trf = models.ForeignKey(TRF, related_name='registration_trf', on_delete=models.CASCADE)
    date_of_recived = models.DateField(default=timezone.now)
    # test_method = models.CharField(max_length=255, null=True)
    received_quantity = models.IntegerField(default=0)
    expectation_delivery_date = models.DateField(default=timezone.now)
    sample_condition = models.CharField(choices=SAMPLE_CONDITION,max_length=50,)
    sample_quantity = models.CharField(choices=SAMPLE_QUANTITY,max_length=50)

    mode_of_recived = models.CharField(choices=MODE_OF_RECEIVED,max_length=50)
    received_by = models.CharField(max_length=255)
    reviewed_and_approved = models.CharField(max_length=255)

    test_parameters_under_NABL_scope = models.CharField(choices=NABL,max_length=20)
    test_parameters_under_CDSCO = models.CharField(choices=CDSCO,max_length=20)




class SampleDetail(models.Model):
    registration = models.ForeignKey(
        Registration, related_name="registration_sample", on_delete=models.CASCADE
    )
    sample_name = models.CharField(max_length=255)
    batch_or_lot_no = models.CharField(max_length=255)
    manufactured_date = models.DateField()
    expiry_date = models.DateField()
    batch_size = models.IntegerField()
    received_quantity = models.IntegerField()