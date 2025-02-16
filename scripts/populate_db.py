import os
import django
from faker import Faker
from users.models import User
from contacts.models import Contact
from spam.models import SpamReport

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spam_detection.settings')
django.setup()

fake = Faker()


def Create_Fake_Users(num_users=10):
    users = []
    for _ in range(num_users):
        user = User.objects.create_user(
            username=fake.user_name(),
            phone_number=fake.phone_number(),
            email=fake.email(),
            password='password123'
        )
        users.append(user)
    print("{} users created successfully!".format(num_users))
    return users


def Create_Fake_Contacts(users, num_contacts_per_user=5):
    for user in users:
        for _ in range(num_contacts_per_user):
            Contact.objects.create(
                name=fake.name(),
                phone_number=fake.phone_number(),
                email=fake.email(),
                added_by=user
            )
    print("{} contacts added for each user ".format(num_contacts_per_user))



def Create_Fake_Spam_Reports(users, num_spam_reports=3):
    for _ in range(num_spam_reports):
        SpamReport.objects.create(
            phone_number=fake.phone_number(),
            reported_by=fake.random_element(users)
        )
    print("{} spam reports created".format(num_spam_reports))


if __name__ == "__main__":
    print("Populating database with fake data ")
    users = Create_Fake_Users(10)
    Create_Fake_Contacts(users, 5)
    Create_Fake_Spam_Reports(users, 3)
    print("Database population complete")
