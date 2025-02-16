from django.core.exceptions import ValidationError
import re

def validate_phone_number(value):
    if not re.match(r'^[0-9]{10}$', value):
        raise ValidationError('Phone number must be exactly 10 digits.')