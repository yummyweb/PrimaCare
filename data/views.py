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
        return redirect('DoctorDashboard')

def DocumentsDashboard(request):
    try:
        patient = Patient.objects.get(user=request.user)

        documents = Document.objects.filter(patient=patient)

        context = {
            "documents": documents
        }

        return render(request, 'data/documentsdashboard.html', context)

    except:
        return redirect('DoctorDashboard')

def ManageDoctorDashboard(request):
    try:
        patient = Patient.objects.get(user=request.user)

        context = {
            "doctors": patient.doctors
        }

        return render(request, 'data/doctor.html', context)

    except:
        return redirect('DoctorDashboard')

def CreateMedicine(request):
    if request.method == 'POST':
        patient = Patient.objects.get(user=request.user)
        createdMedicine = Medicine.objects.create(
            patient=patient,
            name=request.POST['name'],
            quantity=request.POST['quantity'],
            timePeriod=request.POST['time']
        )
        return redirect('Medicine')
    
    return render(request, 'data/medicinecreation.html')

def CreateDocument(request):
    if request.method == 'POST':
        patient = Patient.objects.get(user=request.user)
        file = request.FILES['file']
        createdDocument = Document.objects.create(
            patient=patient,
            name=request.POST['name']
        )
        createdDocument.file = file
        createdDocumentD.save()
        return redirect('Documents')
    
    return render(request, 'data/documentcreation.html')

def DoctorDashboard(request):
    doctor = Doctor.objects.get(user=request.user)

    context = {
        "user": doctor
    }

    return render(request, 'data/doctordashboard.html', context)

