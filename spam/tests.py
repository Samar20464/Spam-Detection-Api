from django.test import TestCase
from .models import SpamReport
from django.contrib.auth import get_user_model

class SpamModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')

    def test_create_spam_report(self):
        spam = SpamReport.objects.create(phone_number='9876543210', reported_by=self.user)
        self.assertEqual(spam.phone_number, '9876543210')
        self.assertEqual(spam.reported_by.username, 'testuser')