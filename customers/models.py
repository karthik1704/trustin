from django.db import models

# Create your models here.
class Customer(models.Model):
    # branch = ?

    customer_name = models.CharField(max_length=255)
    customer_address_line1 = models.CharField(max_length=255,blank=True, default='')
    customer_address_line2 = models.CharField(max_length=255,blank=True, default='')
    website = models.URLField()
    email =  models.EmailField(unique=True)

    nature_of_business = models.CharField(max_length=255)
    product_details = models.CharField(max_length=255)
    market = models.CharField(max_length=255)
    regulatory = models.CharField(max_length=255)
    pan =  models.CharField(max_length=50, blank=True, null=True)
    gst =  models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.customer_name
    

class ContactPerson(models.Model):
    customer = models.ForeignKey(Customer, related_name='contact_detail', on_delete=models.CASCADE)
    person_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=19)
    landline_number = models.CharField(max_length=19, blank=True, null=True)
    email =  models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.person_name
   