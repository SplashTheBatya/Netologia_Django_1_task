# TODO: опишите сериализаторы
from rest_framework import serializers
from measurements.models import *


class ProjectViewSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)


    class Meta:
        model = Project
        fields = '__all__'


class MeasurementViewSerializer(serializers.ModelSerializer):
    value = serializers.CharField(required=True)

    class Meta:
        model = Measurement
        fields = '__all__'
