from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .models import Patients,Appointment,Prescription,Room
from .forms import PatientsForm,AppointmentForm,PrescriptionForm,RoomForm

# Create your views here.

def Patients_create_view(request):
    form = PatientsForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponse('The file is saved')
    form = PatientsForm()
    context = {
        'form':form
    }
    return render(request,'patients/patients_create.html',context)

def Patients_update_view(request,pk):
    patients=get_object_or_404(Patients,pk=pk)
    form = PatientsForm(request.POST or None,instance=patients)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request,'patients/patients_update.html',context)

def Patients_delete_view(request,pk):
    patients = get_object_or_404(Patients,pk=pk)
    if request.method == 'POST':
        patients.delete()
        return redirect(reverse('patients:patients_list_view'))
    context = {
        'patients':patients
    }
    return render(request,'patients/patients_delete.html',context)

def Patients_list_view(request):
    patients = Patients.objects.all()
    context = {
        'patients':patients
    }
    return render(request,'patients/patients_list.html',context)

def Patients_detail_view(request,pk):
    patients = get_object_or_404(Patients,pk=pk)
    context={
        'patients':patients
    }
    return render(request,'patients/patients_detail.html',context)
#############################
def Appointment_create_view(request):
    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        form.save()
    form = AppointmentForm()
    context = {
        'form':form
    }
    return render(request,'patients/appointment_create.html',context)

def Appointment_update_view(request,pk):
    appointment=get_object_or_404(Appointment,pk=pk)
    form = AppointmentForm(request.POST or None,instance=appointment)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request,'patients/appointment_update.html',context)

def Appointment_delete_view(request,pk):
    appointment = get_object_or_404(Appointment,pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect(reverse('patients:appointment_list_view'))
    context = {
        'appointment':appointment
    }
    return render(request,'patients/appointment_delete.html',context)

def Appointment_list_view(request):
    appointment = Appointment.objects.all()
    context = {
        'appointment':appointment
    }
    return render(request,'patients/appointment_list.html',context)

def Appointment_detail_view(request,pk):
    appointment = get_object_or_404(Appointment,pk=pk)
    context={
        'appointment':appointment
    }
    return render(request,'patients/appointment_detail.html',context)
#######################
def Prescription_create_view(request):
    form = PrescriptionForm(request.POST or None)
    if form.is_valid():
        form.save()
    form = PrescriptionForm()
    context = {
        'form':form
    }
    return render(request,'patients/prescription_create.html',context)

def Prescription_update_view(request,pk):
    prescription=get_object_or_404(Prescription,pk=pk)
    form = PrescriptionForm(request.POST or None,instance=prescription)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request,'patients/prescription_update.html',context)

def Prescription_delete_view(request,pk):
    prescription = get_object_or_404(Prescription,pk=pk)
    if request.method == 'POST':
        prescription.delete()
        return redirect(reverse('patients:prescription_list_view'))
    context = {
        'prescription':prescription
    }
    return render(request,'patients/prescription_delete.html',context)

def Prescription_list_view(request):
    prescription = Prescription.objects.all()
    context = {
        'prescription':prescription
    }
    return render(request,'patients/prescription_list.html',context)

def Prescription_detail_view(request,pk):
    prescription = get_object_or_404(Prescription,pk=pk)
    context={
        'prescription':prescription
    }
    return render(request,'patients/prescription_detail.html',context)