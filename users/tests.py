from django.test import TestCase
from .models import User



class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', phone_number='1234567890', password='testpass')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpass'))