from django.db import models
from django.utils import timezone
from accounts.models import Hod

from branches.models import Branch
from samples.models import Product

# 

MARKETING_STATUS =  (
    ('', ''),
    ('MAIL_SENT', 'Mail Sent'),
    ('ENQUIRES_RECEIVED', 'Enquires Received'),
    ('QUOTE_SENT', 'Quote Sent'),
    ('MARKETINT_PLAN', 'Marketint Plan'),
    ('SITE_VISITED', 'Site Visited'),
    ('LAB_VISIT_PLAN', 'Lab Visit Plan'),
    ('LAB_VISITED', 'Lab Visited'),
    ('FOLLOWUP', 'Followup'),
    ('WON', 'Won'),
    ('WIP', 'Work in Progress'),
    ('HOLD', 'Hold'),
    ('LOST', 'Lost'),
    ('SAMPLE_RECEIVED', 'Sample Received'),
)

# Create your models here.
class Customer(models.Model):
    branch = models.ForeignKey(Branch, related_name='customer_branch',on_delete=models.CASCADE)

    customer_code = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    company_id = models.CharField(max_length=255, editable=False)
    customer_address_line1 = models.CharField(max_length=255,blank=True, default='')
    customer_address_line2 = models.CharField(max_length=255,blank=True, default='')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode_no = models.CharField(max_length=100)
    website = models.URLField()
    email =  models.EmailField()


    nature_of_business = models.CharField(max_length=255)
    product_details = models.CharField(max_length=255)
    market = models.CharField(max_length=255)
    regulatory = models.CharField(max_length=255)
    pan =  models.CharField(max_length=50, blank=True, null=True)
    gst =  models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.company_name
    

class ContactPerson(models.Model):
    customer = models.ForeignKey(Customer, related_name='contact_detail', on_delete=models.CASCADE)
    person_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=100)
    landline_number = models.CharField(max_length=19, blank=True, null=True)
    email =  models.EmailField()

    def __str__(self) -> str:
        return self.person_name
   

class CustomerFollowUp(models.Model):
    customer = models.ForeignKey(Customer, related_name='followup_customer', on_delete=models.CASCADE)
    sample = models.ForeignKey(Product, related_name='cus_follow_sample', on_delete=models.DO_NOTHING)
    marketing_status = models.CharField(choices=MARKETING_STATUS, max_length=30)
    assign_to = models.ForeignKey(Hod, on_delete=models.DO_NOTHING,related_name='follow_assign')
    date = models.DateField(default=timezone.now)
    remarks = models.TextField(blank=True, default="")

    def __str__(self) -> str:
        return self.customer.company_name