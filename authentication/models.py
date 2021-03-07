from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username + " - doctor"

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    doctors = models.ManyToManyField(Doctor, blank=True, null=True)
    disease = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(blank=True, null=True)
    profile_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + " - patient"