from django.db import models

# Create your models here.
class TermsAndCondition(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    terms_and_conditions = models.TextField(blank=True, default='')

    def __str__(self) -> str:
        return self.name