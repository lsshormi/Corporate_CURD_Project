from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Company, Employee, Device

# Create your tests here.
class AssetTrackingTestCase(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name='REPLIQ')
        self.employee = Employee.objects.create(name='Lasmin Sultana Shormi', company=self.company)
        self.device = Device.objects.create(type='laptop', condition='Good')

    def test_company_creation(self):
        self.assertEqual(self.company.name, 'REPLIQ')

    def test_employee_creation(self):
        self.assertEqual(self.employee.name, 'Lasmin Sultana Shormi')
        self.assertEqual(self.employee.company, self.company)

    def test_device_creation(self):
        self.assertEqual(self.device.type, 'laptop')
        self.assertEqual(self.device.condition, 'Good')
        
    # Test views and APIs
    def test_company_api(self):
        client = APIClient()
        response = client.get('/companies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_employee_api(self):
        client = APIClient()
        response = client.get('/employees/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_device_api(self):
        client = APIClient()
        response = client.get('/devices/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


 