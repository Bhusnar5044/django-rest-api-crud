from rest_framework import serializers
from .models import Document, Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Employee
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Document
        fields = '__all__'