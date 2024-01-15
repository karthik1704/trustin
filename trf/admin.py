from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from registrations.models import Registration

from trf.models import TRF,  TestingDetail
from trf.views import TRFForm

# Register your models here.
class TestDetailInline(admin.TabularInline):
    model = TestingDetail
    ordering = ('priority_order',)
    extra = 0


class TRFAdmin(admin.ModelAdmin):
    # change_form_template = 'trf/admin/change_form.html'
    inlines = (TestDetailInline,)   
    form = TRFForm
    def change_view(self, request, object_id, form_url='', extra_context=None):
        if '_initiate' in request.POST:
            # Handle the custom action logic
            obj = TRF.objects.get(pk=object_id)
            url = self.initiate_action(request, object_id)
            # Redirect or perform any other actions after the custom action
            # return super().response_change(request,obj,   )
            return HttpResponseRedirect(url)
        return super().change_view(request, object_id, form_url, extra_context)

    def initiate_action(self, request, object_id):
        # Your custom action logic goes here
        # You can access the object using the provided object_id
        trf = TRF.objects.get(pk=object_id)
        obj, created = Registration.objects.get_or_create(trf=trf)
        if created:
            obj.save()

        url = reverse('admin:registrations_registration_change', args=[obj.pk])

        return url
        # Perform your custom action, for example:
     

admin.site.register(TRF, TRFAdmin)