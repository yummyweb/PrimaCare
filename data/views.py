from django.shortcuts import render, redirect
from data.models import Document, Medicine
from authentication.models import Doctor, Patient
import shortuuid
import requests
from data.encryption import crypt

# Create your views here.
def LandingPage(request):
    return render(request, 'data/landing.html')

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

        if request.method == "POST":
            security_key = shortuuid.uuid()[:10]
            patient.security_key = security_key
            patient.save()
            response = requests.post('https://events-api.notivize.com/applications/a1963e82-a8db-41aa-92fd-d53594e4661a/event_flows/02f1c475-4550-4d2e-9526-223aead47ebd/events', json = {
                'access_id': '4358tgf1e',
                'phone': '+12263408677',
                'security_key': security_key
            })
            print(response)

        context = {
            "doctors": patient.doctors.all()
        }

        return render(request, 'data/doctor.html', context)

    except Exception as e:
        print(e)
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
        userAttr = ""
        createdDocument.file = file
        createdDocument.save()
        crypt(createdDocument.file.url, patient.pk, policy=patient.doctors)
        return redirect('Documents')
    
    return render(request, 'data/documentcreation.html')

def DoctorDashboard(request):
    doctor = Doctor.objects.get(user=request.user)

    context = {
        "user": doctor
    }

    return render(request, 'data/doctordashboard.html', context)

def DoctorPatients(request):
    doctor = Doctor.objects.get(user=request.user)
    patients = Patient.objects.all()

    currentPatients = []

    for p in patients:
        for d in p.doctors.all():
            if d == doctor:
                currentPatients.append(p)

    context = {
        "patients": currentPatients
    }

    return render(request, 'data/doctorpatients.html', context)

def PatientAccess(request):
    try:
        if request.method == "POST":
            doctor = Doctor.objects.get(user=request.user)
            try:
                patient = Patient.objects.get(
                    pk=request.POST['phrid'],
                    security_key=request.POST['security_key']
                )
                patient.doctors.add(doctor)
            except:
                return render(request, 'data/patientaccessform.html', {"message": "Error! Invalid credentials."})
    except:
        return redirect('Doctor')

    return render(request, 'data/patientaccessform.html')