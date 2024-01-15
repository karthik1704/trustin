from rest_framework import serializers

from samples.models import Product, TestingParameter, TestType

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class TestTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model=TestType
        fields='__all__'

class TestingParameterSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    test_type = TestTypeSerializer(read_only=True)
    class Meta:
        model = TestingParameter
        fields = '__all__'