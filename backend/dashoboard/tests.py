from django.test import TestCase
from .models import FinancialRecord

class FinancialRecordTestCase(TestCase):

    def setUp(self):
        FinancialRecord.objects.create(title="Test Record", amount=100.0)

    def test_financial_record_creation(self):
        record = FinancialRecord.objects.get(title="Test Record")
        self.assertEqual(record.amount, 100.0)
