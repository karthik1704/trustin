from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from samples.serializers import TestingParameterSerializer


# Create your views here.
class TestParameterListView(ListAPIView):
    serializer_class = TestingParameterSerializer
    model = serializer_class.Meta.model



    def get_queryset(self):
        product_id = self.kwargs["product_id"]
        test_types_params = self.request.GET.getlist('test_type')

        if not test_types_params :
            return self.model.objects.none()
        
        test_types = ' '.join(test_types_params).split(',')

        return self.model.objects.filter(product=product_id,test_type__in=test_types)
