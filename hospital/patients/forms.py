from django import forms
from django.forms import fields
from .models import Patients,Appointment,Prescription,Room

class PatientsForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields= '__all__'

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields= '__all__'

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields= '__all__'

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields= '__all__'
