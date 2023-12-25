from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView
from rest_framework import permissions

from customers.models import Customer
# Create your views here.
class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields='__all__'


class CustomerRetrieveView(RetrieveAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = (permissions.AllowAny,)
    