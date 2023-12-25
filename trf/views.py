from typing import Any
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.generics import ListAPIView
from samples.models import PARA_TEST_TYPE, TestingParameter
from trf.models import TRF, SampleDetail, TestingDetail
from trf.serializers import TestingDetailSerilaizer
# Create your views here.

class SampleDetailForm(forms.ModelForm):

    class Meta:
        model = SampleDetail
        exclude=('trf',)

class TestingDetailForm(forms.ModelForm):
    trf_code = forms.HiddenInput()
    class Meta:
        model = TestingDetail
        exclude=('trf',)

class TRFForm(forms.ModelForm):
    test_type = forms.MultipleChoiceField(choices=PARA_TEST_TYPE, widget=forms.CheckboxSelectMultiple(), )

    # sample_details = forms.formset_factory(SampleDetailForm)
    # testings = forms.modelformset_factory(TestingDetail,TestingDetailForm, )
    class Meta:
        model = TRF
        exclude = ('date_of_registration',)


    def save(self, commit: bool = ...) -> Any: # type: ignore
        return super().save(commit)

TestFormSet = forms.inlineformset_factory(TRF,TestingDetail, TestingDetailForm, )
def customerTRFView(request, trf_code):
    customer = None
    if trf_code:
        customer = get_object_or_404(TRF, trf_code=trf_code)

    if request.method == 'POST':
        form = TRFForm(request.POST, instance=customer)
        formset = TestFormSet(request.POST, instance=customer,prefix='testing')
    
        if form.is_valid() and formset.is_valid():
           
            form.save()
            formset.save()

            return redirect('.')  # Redirect to a customer list view
    else:
        form = TRFForm(instance=customer)
        formset = TestFormSet(instance=customer, prefix='testing')
    return render(request, 'trf/trf.html', {'form': form, 'formset':formset , 'trf_code': trf_code})



MyFormSet = forms.inlineformset_factory(TRF,TestingDetail,TestingDetailForm, )

def testformsetView(request):

    if request.method == 'POST':
        formset = MyFormSet(request.POST, prefix="testing")
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data)
            # form.save()
            return redirect('.')  # Redirect to a customer list view
    else:
        formset = MyFormSet(prefix="testing")

    return render(request, 'trf/test.html', {'formset': formset, })


class TestingDetailListView(ListAPIView):
    serializer_class = TestingDetailSerilaizer
    model = serializer_class.Meta.model
 
    def get_queryset(self):
        trf_code = self.kwargs["trf_code"]
        return self.model.objects.filter(trf__trf_code=trf_code)
