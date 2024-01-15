from typing import Any
from django.contrib import admin
from django.http import HttpRequest

from registrations.models import SampleDetail,   Registration
from trf.models import TestingDetail

# Register your models here.
class SampleDetailInline(admin.StackedInline):
    model=SampleDetail
    extra = 0

class TestDetailInline(admin.TabularInline):
    model=TestingDetail
    extra = 0
    fk_name = 'registration__trf'

    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        return False

class RegistrationAdmin(admin.ModelAdmin):
    inlines = (SampleDetailInline,TestDetailInline,)


admin.site.register(Registration, RegistrationAdmin)