from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def Doctor(request):
    if request.method == "POST":
        if 'email' in request.POST:
            user = User.objects.create(
                username=request.POST['username'], 
                email=request.POST['email'],
                is_doctor=True,
                specialization=request.POST['specialization']
            )
            user.set_password(request.POST['password'])
            user.save()
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("Dashboard") 

    return render(request, 'authentication/doctor.html')

def Patient(request):
    if request.method == "POST":
        if 'email' in request.POST:
            user = User.objects.create(
                username=request.POST['username'], 
                email=request.POST['email'],
                is_doctor=False
            )
            user.set_password(request.POST['password'])
            user.save()
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("Dashboard")

    return render(request, 'authentication/patient.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("Register")

    return render(request, 'authentication/login.html')

def Dashboard(request, id):
    user = request.user

    context = {
        "user": user
    }

    return render(request, 'authentication/user.html', context)