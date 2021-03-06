from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Patient, Doctor

# Create your views here.
def DoctorAuth(request):
    if request.method == "POST":
        if 'email' in request.POST:
            user = User.objects.create(
                username=request.POST['username'], 
                email=request.POST['email'],
                is_doctor=True,
            )
            user.set_password(request.POST['password'])
            user.save()

            doctor = Doctor.objects.create(
                user=user,
                specialization=request.POST['specialization']
            )
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("Dashboard") 

    return render(request, 'authentication/doctor.html')

def PatientAuth(request):
    if request.method == "POST":
        if 'email' in request.POST:
            user = User.objects.create(
                username=request.POST['username'], 
                email=request.POST['email'],
                is_doctor=False
            )
            user.set_password(request.POST['password'])
            user.save()

            patient = Patient.objects.create(
                user=user
            )
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("Dashboard")

    return render(request, 'authentication/patient.html')

def Dashboard(request, id):
    user = request.user

    if not user:
        return redirect("PatientAuth")

    context = {
        "user": user
    }

    return render(request, 'authentication/dashboard.html', context)