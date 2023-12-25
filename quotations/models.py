from django.db import models
from django.utils import timezone
from branches.models import Branch
from customers.models import Customer
from notes.models import Note
from samples.models import Product
from terms.models import TermsAndCondition

# Create your models here.
SINGLE='SINGLE'
DOUBLE = 'DOUBLE'
Q_TYPE = ((SINGLE, 'Single Page'), (DOUBLE, 'Double Page'))

BATCH= 'BATCH'
SIZE = 'SIZE'
CHARGE_TYPE = ((BATCH, 'Batch'), (SIZE, 'Size'))

class Quotation(models.Model):
    q_type = models.CharField(choices=Q_TYPE, max_length=50, default=SINGLE)
    quotation_id = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, related_name='quotation_branch', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    customer= models.ForeignKey(Customer, related_name='quotation_customer', on_delete=models.CASCADE)
    sample_name = models.CharField(max_length=255)
    required_quantity= models.CharField(max_length=255)
    turn_around_time = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    body = models.TextField(default='')
    terms_and_condition = models.ForeignKey(TermsAndCondition, related_name='quotation_terms', on_delete=models.DO_NOTHING)
    note = models.ForeignKey(Note, related_name='quotation_note', on_delete=models.DO_NOTHING)

    charges_per = models.CharField(choices=CHARGE_TYPE, max_length=50)

    product =  models.ForeignKey(Product, related_name="quotation_product", on_delete=models.DO_NOTHING)
    no_of_test = models.PositiveIntegerField() 
    total_amount =  models.DecimalField(decimal_places=4, max_digits=19)
    discount_percentage = models.DecimalField(decimal_places=2, max_digits=4)
    discount_amount = models.DecimalField(decimal_places=4, max_digits=19)
    total_amount_before_tax = models.DecimalField(decimal_places=4, max_digits=19)

