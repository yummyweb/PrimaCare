from django.urls import path 
from data.views import (CreateDocument, CreateMedicine, DoctorDashboard, DocumentsDashboard,
    LandingPage, ManageDoctorDashboard, MedicationsDashboard, PatientAccess, UserDashboard)

urlpatterns = [
    path('', LandingPage, name="Landing"),
    path('dashboard/patient/', UserDashboard, name="User"),
    path('medicine/', MedicationsDashboard, name="Medicine"),
    path('document/', DocumentsDashboard, name="Documents"),
    path('doctors/', ManageDoctorDashboard, name="Doctor"),
    path('medicine/create/', CreateMedicine, name="CreateMedicine"),
    path('document/create/', CreateDocument, name="CreateDocument"),
    path('dashboard/doctor/', DoctorDashboard, name="DoctorDashboard"),
    path('patient-access/', PatientAccess, name="PatientAccess")
]