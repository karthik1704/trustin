from django.db import models
from django.utils import timezone
from branches.models import Branch
from customers.models import Customer
from samples.models import Product, TestingParameter
from samples.models import PARA_TEST_TYPE
# Create your models here.
class TRF(models.Model):
    trf_code = models.CharField(max_length=255, editable=False)
    branch = models.ForeignKey(Branch, related_name='trf_branch',on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='trf_customer', on_delete=models.DO_NOTHING)
 
    
    
    date_of_registration = models.DateField(default=timezone.now)
    date_of_recived = models.DateField(default=timezone.now)
    test_type = models.CharField(choices=(PARA_TEST_TYPE), max_length=50)
    test_method = models.CharField(max_length=255, null=True)
    sample_id = models.CharField(max_length=255, null=True)
    sample_name = models.CharField(max_length=255, null=True)
    description = models.TextField(default='',blank=True ) 
    manufactured_by = models.CharField(max_length=255, null=True)
    batch_or_lot_no = models.CharField(max_length=255, null=True)
    manufactured_date = models.DateField(null=True)
    expiry_date = models.DateField(null=True)
    batch_size = models.IntegerField(default=0)
    received_quantity = models.IntegerField(default=0)
    expectation_delivery_date = models.DateField(default=timezone.now)
    format_name = models.CharField(max_length=255)
    nabl_logo = models.BooleanField(default=False)
    no_of_samples = models.IntegerField(default=0)

    # 
    product = models.ForeignKey(Product, related_name='trf_product', on_delete=models.DO_NOTHING, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.trf_code

class SampleDetail(models.Model):
    trf = models.ForeignKey(TRF, related_name='trf_sample_detail', on_delete=models.CASCADE)
    sample_name = models.CharField(max_length=255)
    batch_or_lot_no = models.CharField(max_length=255)
    manufactured_date = models.DateField()
    expiry_date = models.DateField()
    batch_size = models.IntegerField()
    received_quantity = models.IntegerField()

class TestingDetail(models.Model):
    trf = models.ForeignKey(TRF, related_name='trf_testing', on_delete=models.CASCADE)
    test= models.ForeignKey(TestingParameter, related_name='trf_test', on_delete=models.DO_NOTHING)
    priority_order = models.IntegerField()
    