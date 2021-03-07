from django.urls import path 
from data.views import (CreateDocument, CreateMedicine, DoctorDashboard, DocumentsDashboard,
    MedicationsDashboard, UserDashboard)

urlpatterns = [
    path('dashboard/patient/', UserDashboard, name="User"),
    path('medicine/', MedicationsDashboard, name="Medicine"),
    path('document/', DocumentsDashboard, name="Documents"),
    path('medicine/create/', CreateMedicine, name="CreateMedicine"),
    path('document/create/', CreateDocument, name="CreateDocument"),
    path('dashboard/doctor/', DoctorDashboard, name="DoctorDashboard")
]