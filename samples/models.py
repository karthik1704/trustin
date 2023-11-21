from django.db import models
from django.utils.translation import gettext_lazy as _

from branches.models import Branch

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(_("Product/Sample Name"), max_length=255)
    description = models.TextField(blank=True, default="")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.product_name


TESTING = "TESTING"
SERVICE = "SERVICE"
PARA_TEST_TYPE = ((TESTING, "Testing"), (SERVICE, "Service"))


class TestingParameter(models.Model):
    branch = models.ForeignKey(
        Branch, related_name="parameter_branch", on_delete=models.CASCADE
    )
    parameter_code = models.CharField(max_length=255, editable=False)
    test_type = models.CharField(choices=(PARA_TEST_TYPE), max_length=50)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="para_product",
    )
    method_or_spec = models.CharField(
        _("Method / Specification"), max_length=255, blank=True, null=True
    )
    amount = models.DecimalField(
        _("Amount"), max_digits=19, decimal_places=4, blank=True, null=True
    )
    method_or_spec = models.CharField(
        _("Method / Specification"), max_length=255, blank=True, null=True
    )

    group_of_test_parameters = models.TextField(blank=True, default='')
