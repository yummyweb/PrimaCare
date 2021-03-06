from django.urls import path 
from authentication.views import Doctor, Patient, Dashboard

urlpatterns = [
    path('auth/doctor/', Doctor, name="Doctor"),
    path('auth/patient/', Patient, name="Patient"),
    path('dashboard/', Dashboard, name="Dashboard")
]