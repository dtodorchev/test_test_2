from django.core.exceptions import ValidationError
from django.db import models
import re

def validate_username(value):
    if not re.match(r'^\w+$', value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")

class Profile(models.Model):
    username = models.CharField(max_length=15, validators=[validate_username])
    email = models.EmailField()
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username