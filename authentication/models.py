from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
SPECIALIZATION_CHOICES = (
    ("eyes", "eyes"),
    ("heart", "heart"),
    ("blood", "blood"),
    ("respiratory", "respiratory"),
)

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    specialization = models.CharField(max_length=200, null=True, blank=True, choices=SPECIALIZATION_CHOICES)

    def __str__(self):
        return self.username