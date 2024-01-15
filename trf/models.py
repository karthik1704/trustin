from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from branches.models import Branch
from customers.models import Customer
from samples.models import Product, TestType, TestingParameter
from samples.models import PARA_TEST_TYPE

# Create your models here.

TESTING_PROCESS = [
    ("BATCH_ANALYSIS", "Batch Analysis"),
    ("METHOD_DEVELOPMENT", "Method Development"),
    ("METHOD_VALIDATION", "Method Validation"),
    ("RD_RESEARCH", "R&D / Research"),
    ("REGULATORY", "Regulatory"),
]
SAMPLING_BY = [("CUSTOMER", "Customer"), ("LABORATORY", "Laboratory")]

DISPOSAL_PROCESS = (("DISCARD", "Discard"), ("RETURN", "Return"))
REPORT_SENT_BY = (("COURIER", "Courier"), ("EMAIL", "E-mail"))
Yes_OR_NO = (("YES", "Yes"), ("NO", "No"))
DOCUMENTS_TYPE = [
    ("MSDS", "MSDS"),
    ("COA", "COA"),
    ("IFU", "IFU"),
    ("IF_ANY_OTHER", "If any other"),
]


class TRF(models.Model):
    trf_code = models.CharField(max_length=255, editable=False)
    branch = models.ForeignKey(
        Branch, related_name="trf_branch", on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        Customer, related_name="trf_customer", on_delete=models.DO_NOTHING
    )

    date_of_registration = models.DateField(default=timezone.now)
    test_type = models.ManyToManyField(TestType)
    sample_id = models.CharField(max_length=255, null=True)
    sample_name = models.CharField(max_length=255, null=True)
    description = models.TextField(default="", blank=True)
    manufactured_by = models.CharField(max_length=255, null=True)
    batch_or_lot_no = models.CharField(max_length=255, null=True)
    manufactured_date = models.DateField(null=True)
    expiry_date = models.DateField(null=True)
    batch_size = models.IntegerField(default=0)
    format_name = models.CharField(max_length=255, null=True)
    nabl_logo = models.BooleanField(default=False)
    no_of_samples = models.IntegerField(default=0)

    sample_storage_condition = models.TextField(blank=True, default="")
    sampling_by = models.CharField(choices=SAMPLING_BY, max_length=50, null=True) 
    testing_process = ArrayField(
        models.CharField(
            choices=TESTING_PROCESS,
            max_length=100,
        ),
        null=True,
    )
    sample_disposal_process = models.CharField(
        choices=DISPOSAL_PROCESS, max_length=100, null=True
    )
    report_sent_by = ArrayField(
        models.CharField(
            choices=REPORT_SENT_BY,
            max_length=100,
        ),
        null=True,
    )

    fail_statement_sent = models.CharField(verbose_name="Conformity(Passes/ Fail)statement required",choices=Yes_OR_NO, max_length=100)
    specific_decision_rule = models.CharField(verbose_name='Do you need any specific decision rule to be followed by the laboratory?',choices=Yes_OR_NO, max_length=100)
    binary_decision_rule = models.CharField(verbose_name='Lab follows binary decision rule of sample accepance (w=0) do you accept?',choices=Yes_OR_NO, max_length=100)

    submission_of_documents = ArrayField(
        models.CharField(choices=DOCUMENTS_TYPE, max_length=100,), null=True
    )
    #
    product = models.ForeignKey(
        Product, related_name="trf_product", on_delete=models.DO_NOTHING, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.trf_code




class TestingDetail(models.Model):
    trf = models.ForeignKey(TRF, related_name="trf_testing", on_delete=models.CASCADE)
    test = models.ForeignKey(
        TestingParameter, related_name="trf_test", on_delete=models.DO_NOTHING
    )
    priority_order = models.IntegerField()
