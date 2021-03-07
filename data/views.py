from django.shortcuts import render, redirect
from data.models import Document, Medicine
from authentication.models import Doctor, Patient

# Create your views here.
def UserDashboard(request):
    try:
        patient = Patient.objects.get(user=request.user)

        context = {
            "user": patient
        }
        
    except:
        return redirect('DoctorDashboard')
    
    return render(request, 'data/userdashboard.html', context) 

def MedicationsDashboard(request):
    try:
        patient = Patient.objects.get(user=request.user)

        medications = Medicine.objects.filter(patient=patient)

        context = {
            "medications": medications
        }

        return render(request, 'data/medicinedashboard.html', context)

    except:
        return redirect('User')

def DocumentsDashboard(request):
    try:
        patient = Patient.objects.get(user=request.user)

        documents = Document.objects.filter(patient=patient)

        context = {
            "documents": documents
        }

        return render(request, 'data/documentsdashboard.html', context)

    except:
        return redirect('User')

def DoctorDashboard(request):
    doctor = Doctor.objects.get(user=request.user)

    context = {
        "user": doctor
    }

    return render(request, 'data/doctordashboard.html', context)

