# tests.py

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

class YourAppAPITest(TestCase):
    def setUp(self):
        # Set up your test data here

    def test_invoice_api(self):
        # Write test cases for the /invoices/ API

    def test_invoice_detail_api(self):
        # Write test cases for the /invoices/<int:pk>/ API
