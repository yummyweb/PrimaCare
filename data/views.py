from django.shortcuts import render
from data.models import Medicine
from authentication.models import Doctor, Patient

# Create your views here.
def UserDashboard(request):
    patient = Patient.objects.get(user=request.user)
    
    if not patient:
        doctor = Doctor.objects.get(user=request.user)

        context = {
            "user": doctor,
            "id_doctor": True
        }
    else:
        context = {
            "user": patient,
            "is_doctor": False
        }
    
    return render(request, 'data/userdashboard.html', context) 

def Medications(request):
    patient = Patient.objects.filter(user=request.user)
    medications = Medicine.objects.filter(patient=patient)

    context = {
        "medications": medications
    }

    return render(request, 'data/medicine.html', context)