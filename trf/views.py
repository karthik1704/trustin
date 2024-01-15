from typing import Any
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from rest_framework.generics import ListAPIView
from samples.models import PARA_TEST_TYPE, TestingParameter
from trf.models import DOCUMENTS_TYPE, REPORT_SENT_BY, SAMPLING_BY, TESTING_PROCESS, TRF,  TestingDetail
from trf.serializers import TestingDetailSerilaizer

# Create your views here.




class TestingDetailForm(forms.ModelForm):
    trf_code = forms.HiddenInput()

    class Meta:
        model = TestingDetail
        exclude = ("trf", "id")


class TRFForm(forms.ModelForm):
    # sampling_by = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple, choices=SAMPLING_BY
    # )
    testing_process = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=TESTING_PROCESS
    )
    submission_of_documents = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=DOCUMENTS_TYPE
    )
    report_sent_by = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=REPORT_SENT_BY
    )
    # test_type = forms.MultipleChoiceField(choices=PARA_TEST_TYPE, widget=forms.CheckboxSelectMultiple(), )

    # sample_details = forms.formset_factory(SampleDetailForm)
    # testings = forms.modelformset_factory(TestingDetail,TestingDetailForm, )
    class Meta:
        model = TRF
        exclude = ("date_of_registration",)
        widgets = {
            "test_type": forms.CheckboxSelectMultiple,
            "manufactured_date": forms.DateInput(attrs={"type": "date"}),
            "expiry_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super(TRFForm, self).__init__(*args, **kwargs)

        # Set the 'is_disabled' field to be disabled
        # self.fields['branch'].widget.attrs['disabled'] = True
        # self.fields['customer'].widget.attrs['disabled'] = True
        # # self.fields['customer'].widget.attrs['disabled'] = True

    # def clean(self) -> dict[str, Any]:
    #     cleaned_data = super().clean()
    #     sampling_by = cleaned_data.get('sampling_by')
    #     testing_process = cleaned_data.get('testing_process')
    #     print(sampling_by)
    #     print(testing_process)
    #     if sampling_by is not None:
    #         cleaned_data['sampling_by'] = ",".join(sampling_by)
    #     if testing_process is not None:
    #         cleaned_data['testing_process'] = ",".join(testing_process)
    #     print(type(sampling_by))
    #     print(type(cleaned_data['sampling_by']))
    #     print(type(testing_process))
    #     print(type(cleaned_data['testing_process']))
    #     print( cleaned_data['sampling_by'])
    #     print( cleaned_data['testing_process'])

    #     return cleaned_data

    def save(self, commit: bool = ...) -> Any:  # type: ignore
        return super().save(commit)


TestFormSet = forms.inlineformset_factory(
    TRF,
    TestingDetail,
    TestingDetailForm,
)


def customerTRFView(request, trf_code):
    customer = None
    if trf_code:
        customer = get_object_or_404(TRF, trf_code=trf_code)

    if request.method == "POST":
        form = TRFForm(request.POST, instance=customer)
        formset = TestFormSet(request.POST, instance=customer, prefix="testing")

        
        if form.is_valid() and formset.is_valid():
            form.save()
            print(formset.cleaned_data)
            formset.save()

            return redirect(reverse("trf:trf_success"))
            # return redirect(".")
        else:

            # print('You got errors')
            print(form.errors)
            # print('formset')
            print(formset.errors)
    else:
        form = TRFForm(instance=customer)
        formset = TestFormSet(instance=customer, prefix="testing")
    return render(
        request,
        "trf/trf.html",
        {"form": form, "formset": formset, "trf_code": trf_code},
    )


def trf_success(request):

    return render(request, 'trf/trf_success.html')


MyFormSet = forms.inlineformset_factory(
    TRF,
    TestingDetail,
    TestingDetailForm,
)


def testformsetView(request):
    if request.method == "POST":
        formset = MyFormSet(request.POST, prefix="testing")
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data)
            # form.save()
            return redirect("trf/trf_success.html")  # Redirect to a customer list view
    else:
        formset = MyFormSet(prefix="testing")

    return render(
        request,
        "trf/test.html",
        {
            "formset": formset,
        },
    )


class TestingDetailListView(ListAPIView):
    serializer_class = TestingDetailSerilaizer
    model = serializer_class.Meta.model

    def get_queryset(self):
        trf_code = self.kwargs["trf_code"]
        return self.model.objects.filter(trf__trf_code=trf_code).order_by(
            "priority_order"
        )
