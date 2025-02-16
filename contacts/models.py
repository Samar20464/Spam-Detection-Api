from django.db import models
from django.conf import settings

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(blank=True, null=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.name, self.phone_number)
