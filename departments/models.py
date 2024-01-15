from django.db import models
from accounts.models import Hod

from samples.models import TestType

# Create your models here.
class Department(models.Model):
    test_type = models.ForeignKey(TestType, on_delete=models.CASCADE, related_name='department_test_type')
    hod = models.ForeignKey(Hod, on_delete=models.CASCADE)