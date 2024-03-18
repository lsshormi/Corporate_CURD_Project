from django.shortcuts import render
from rest_framework import viewsets
from drf_spectacular.openapi import AutoSchema 
from .models import Company, Employee, Device
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    schema = AutoSchema()  # Set schema attribute for drf_spectacular's AutoSchema

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    schema = AutoSchema()  

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    schema = AutoSchema()
