from django.urls import path
from patients.views import (
    Patients_create_view,Patients_delete_view,Patients_detail_view,Patients_update_view,Patients_list_view,
    Appointment_create_view,Appointment_delete_view,Appointment_detail_view,Appointment_list_view,Appointment_update_view,
    Prescription_create_view,Prescription_delete_view,Prescription_detail_view,Prescription_list_view,Prescription_update_view,
)

app_name = 'patients'

urlpatterns = [
    path('patient_create',Patients_create_view,name='patients_create_view'),
    path('patient_list',Patients_list_view,name='patients_list_view'),
    path('<int:pk>/',Patients_detail_view,name='patients_detail_view'),
    path('<int:pk>/update',Patients_update_view,name='patients_update_view'),
    path('<int:pk>/delete',Patients_delete_view,name='patients_delete_view'),

    path('appointment_create',Appointment_create_view,name='appointment_create_view'),
    path('appointment_list',Appointment_list_view,name='appointment_list_view'),
    path('appointment/<int:pk>/',Appointment_detail_view,name='appointment_detail_view'),
    path('appointment/<int:pk>/update',Appointment_update_view,name='appointment_update_view'),
    path('appointment/<int:pk>/delete',Appointment_delete_view,name='appointment_delete_view'),

    path('prescription_create',Prescription_create_view,name='prescription_create_view'),
    path('prescription_list',Prescription_list_view,name='prescription_list_view'),
    path('prescription/<int:pk>/',Prescription_detail_view,name='prescription_detail_view'),
    path('prescription/<int:pk>/update',Prescription_update_view,name='prescription_update_view'),
    path('prescription/<int:pk>/delete',Prescription_delete_view,name='prescription_delete_view'),

]
