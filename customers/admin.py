from django.contrib import admin

from customers.models import ContactPerson, Customer

# Register your models here.
class ContactPersonAdmin(admin.StackedInline):
    model =ContactPerson
    extra = 1
    fk_name = 'customer'

class CustomerAdmin(admin.ModelAdmin):
    inlines = (ContactPersonAdmin,)

admin.site.register(Customer, CustomerAdmin)