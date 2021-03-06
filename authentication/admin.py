from django.contrib import admin
from authentication.models import Doctor, Patient, User

# Register your models here.
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)