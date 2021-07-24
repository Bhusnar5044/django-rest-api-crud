from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class DocumentViewset(viewsets.ModelViewSet):
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer