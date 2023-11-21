from django.db import models

# Create your models here.
class Branch(models.Model):
    branch_name = models.CharField(max_length=255, unique=True)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.PositiveBigIntegerField()
    landline_number = models.CharField(max_length=19, blank=True, null=True)
    email = models.EmailField()
    pan_no = models.CharField(max_length = 20, blank=True, null=True)
    cin = models.CharField(max_length = 50, blank=True, null=True)
    gstin = models.CharField(max_length = 50, blank=True, null=True)
    bank_details = models.CharField(max_length = 255, blank=True, null=True)
    ifsc_code = models.CharField(max_length = 10, blank=True, null=True)
     
    def __str__(self) -> str:
        return self.branch_name