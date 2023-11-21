from django.db import models

# Create your models here.
from django.db import models

from customers.models import Customer
# Create your models here.
TESTING_PROCESS = (
    ('BATCH_ANALYSIS', 'Batch Analysis'),
    ('METHOD_DEVELOPMENT', 'Method Development'),
    ('METHOD_VALIDATION', 'Method Validation'),
    ('RD_RESEARCH', 'R&D / Research'),
    ('REGULATORY', 'Regulatory'),
                   )
SAMPLING_BY = (('CUSTOMER', 'Customer'), ('LABORATORY','Laboratory'))

class SampleRequest(models.Model):
    customer = models.ForeignKey(Customer, related_name='requester', on_delete=models.DO_NOTHING)
    alternate_address = models.TextField(blank=True, default='')
    mfg_license_number = models.CharField(max_length=100, blank=True, null=True)
    po_or_ref_number = models.CharField(max_length=100, blank=True, null=True)
    quotation_number = models.CharField(max_length=100, blank=True, null=True)

    # sample details
    sample_name = models.CharField(max_length=255,)
    sample_name2 = models.CharField(max_length=255, blank=True, null=True)
    sample_description =  models.TextField(blank=True, default='')
    batch_or_lot_number = models.DecimalField(decimal_places=3,max_digits=4 )
    batch_size = models.PositiveIntegerField(blank=True, null=True)
    sterilization_batch_number = models.BigIntegerField(blank=True, null=True)
    sample_quantity_sent = models.CharField(max_length=100,blank=True, null=True)
    date_of_mfg = models.DateField()
    date_of_exp = models.DateField()
    sampling_by = models.CharField(choices=SAMPLING_BY, max_length=50)
    sample_manufactured_by = models.CharField(max_length=255)
    sample_storage_condition = models.CharField(max_length=255, blank=True, null=True)
    testing_process = models.CharField(choices=TESTING_PROCESS, max_length=100)


