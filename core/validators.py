import os

from django.core.exceptions import ValidationError

import re
from django.core.exceptions import ValidationError
from django.core.validators import validate_email as django_validate_email


def validate_email(email):
    """Validate email format."""
    try:
        django_validate_email(email)
    except ValidationError:
        raise ValidationError("Invalid email format")
    return email


def validate_phone(phone):
    pattern = r'^\+?1?\d{9,15}$'
    if not re.match(pattern, phone):
        raise ValidationError("Invalid phone number format. It must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    return phone


def validate_image(image):
    file_size = image.size
    limit_kb = 500
    if file_size > limit_kb * 1024:
        raise ValidationError("Image size exceeds the limit of 500KB.")

    valid_extensions = ['.jpg', '.jpeg', '.png']
    file_extension = os.path.splitext(image.name)[1].lower()
    if file_extension not in valid_extensions:
        raise ValidationError("Invalid file type. Only '.jpg', '.jpeg', and '.png' are allowed.")

    return image
def validate_password_complexity(password):
    """Ensure password meets complexity requirements."""
    if not re.search(r'\d', password):
        raise ValidationError('Password must contain at least one digit.')
    if not re.search(r'[A-Za-z]', password):
        raise ValidationError('Password must contain at least one letter.')
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError('Password must contain at least one special character.')
    return password
