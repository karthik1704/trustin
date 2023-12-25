from rest_framework import serializers
from samples.serializers import TestingParameterSerializer

from trf.models import TestingDetail



class TestingDetailSerilaizer(serializers.ModelSerializer):
    test = TestingParameterSerializer(read_only=True)

    class Meta:
        model= TestingDetail
        fields = '__all__'