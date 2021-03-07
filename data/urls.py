from django.urls import path 
from data.views import DocumentsDashboard, MedicationsDashboard, UserDashboard, DoctorDashboard

urlpatterns = [
    path('dashboard/patient/', UserDashboard, name="User"),
    path('medicine/', MedicationsDashboard, name="Medicine"),
    path('document/', DocumentsDashboard, name="Documents"),
    path('dashboard/doctor/', DoctorDashboard, name="DoctorDashboard")
]