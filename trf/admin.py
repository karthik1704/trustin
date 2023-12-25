from django.contrib import admin

from trf.models import TRF, SampleDetail, TestingDetail

# Register your models here.
class TestDetailInline(admin.TabularInline):
    model = TestingDetail
    ordering = ('priority_order',)
    extra = 0

class SampleDetailInline(admin.TabularInline):
    model = SampleDetail
    extra = 0

class TRFAdmin(admin.ModelAdmin):
    inlines = (TestDetailInline, SampleDetailInline)    
admin.site.register(TRF, TRFAdmin)