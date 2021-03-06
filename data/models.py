from django.db import models
from authentication.models import Patient

# Create your models here.
TIME_PERIOD_CHOICES = (
    ("week", "week"),
    ("day", "day"),
    ("fortnight", "fortnight")
)

class Medicine(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    timePeriod = models.CharField(max_length=200, choices=TIME_PERIOD_CHOICES)

    def __str__(self):
        return self.name + " - " + self.patient.user.username

class Document(models.Model):
   patient = models.OneToOneField(Patient, on_delete=models.CASCADE, primary_key=True)
   name = models.CharField(max_length=200)
   file = models.FileField(upload_to="documents/")
   uploaded_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.name + " - document"