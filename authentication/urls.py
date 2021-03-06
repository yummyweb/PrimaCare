from django.urls import path 
from authentication.views import DoctorAuth, PatientAuth, Dashboard

urlpatterns = [
    path('auth/doctor/', DoctorAuth, name="Doctor"),
    path('auth/patient/', PatientAuth, name="Patient"),
    path('dashboard/', Dashboard, name="Dashboard")
]