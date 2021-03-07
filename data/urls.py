from django.urls import path 
from data.views import UserDashboard

urlpatterns = [
    path('', UserDashboard, name="User"),
]