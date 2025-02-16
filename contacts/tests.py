from django.test import TestCase
from .models import Contact
from django.contrib.auth import get_user_model

class ContactModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')

    def Test_Create_Contact(self):
        contact = Contact.objects.create(name='Rahul', phone_number='123456', added_by=self.user)
        self.assertEqual(contact.name, 'Rahul')
        self.assertEqual(contact.added_by.username, 'testuser')