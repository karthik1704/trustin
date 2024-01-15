from typing import Any
from django import forms
from django.contrib import admin
from django.http.request import HttpRequest
from django.core.mail import send_mail
from branches.models import Branch
from customers.models import ContactPerson, Customer, CustomerFollowUp
from trf.models import TRF
from accounts.config import ROLE_MARKETING

# Register your models here.
class ContactPersonAdmin(admin.StackedInline):
    model =ContactPerson
    # extra = 3
    fk_name = 'customer'
    can_delete=True
    
    # def has_add_permission(self, request, obj) -> bool:
    #     return  True

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ("company_name", 'customer_code',)
    inlines = (ContactPersonAdmin,)
    list_display=('company_name', 'customer_code', 'email')

class CustomerFollowUpForm(forms.ModelForm):
    mail_send = forms.BooleanField(
        widget=forms.CheckboxInput(),
        label="Do you want to send mail",
        required=False,
    )

    subject = forms.CharField(max_length=255, required=False)
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':4, "cols":40, "class":"vLargeTextField"}), required=False)

    class Meta:
        model = CustomerFollowUp
        fields = '__all__'


class CustomerFollowUpAdmin(admin.ModelAdmin):

    change_form_template = "admin/customers/change_form.html"
    autocomplete_fields = ["customer", "sample"]
    readonly_fields = ("customer_code",'customer_address_line1', 'email',)
    form = CustomerFollowUpForm

    fieldsets = (
        ("Customer Information", {"fields": ("customer","customer_code",'customer_address_line1','email')}),
        (
            "FollowUp Details",
            {
                "fields": (
                  "sample",
                  "assign_to",
                  "marketing_status",
                )
            },
        ),

        (
            "Email Information",
            {"fields": ("mail_send", "subject", 'body')},
        ),
        (
            "Other Information",
            {"fields": ("date", "remarks")},
        ),
      
    )


    # class Media:
    #     js = ('customers/js/custom_admin.js',)  

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Filter the queryset based on the currently logged-in user
        if request.user:
            if  request.user.role == ROLE_MARKETING:
                return qs.filter(assign_to=request.user)
        return qs

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        mails = form.cleaned_data["customer"].email
        to_mail = mails.split(',')

        if form.cleaned_data["mail_send"] and (obj.marketing_status == 'MAIL_SENT'):   
            send_mail("Test", "Test code", 'sender@example.com', [to_mail], fail_silently=False)

        if form.cleaned_data["mail_send"]:
            to_mail = obj.customer.email
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["body"]

            send_mail(subject, message, 'sender@example.com', [to_mail], fail_silently=False)

        if not change:
            marketing_status = form.cleaned_data["marketing_status"]
            if marketing_status == 'WON': 
                branch = Branch.objects.get(pk=1)
                instance , created = TRF.objects.get_or_create(branch=branch, customer=obj.customer, product=obj.sample)
                if created:
                    instance.save()
        if change:
            if form.initial["marketing_status"] != form.cleaned_data["marketing_status"]:
                marketing_status = form.cleaned_data["marketing_status"]
                if marketing_status == 'WON': 
                    branch = Branch.objects.get(pk=1)
                    TRF.objects.create(branch=branch, customer=obj.customer,)
        return super().save_model(request, obj, form, change)

    def customer_code(self, obj):
        return obj.customer.customer_code
    
    def customer_address_line1(self, obj):
        return obj.customer.customer_address_line1
    
    def email(self, obj):
        return obj.customer.email

    


admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerFollowUp, CustomerFollowUpAdmin)