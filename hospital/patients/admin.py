from django.contrib import admin
from .models import Patients,Appointment,Prescription,Room
# Register your models here.
admin.site.register(Patients)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Room)