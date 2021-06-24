from django.db import models
from docs.models import Docs

# Create your models here.
class Patients(models.Model):
    name = models.CharField(max_length=32)
    emailid = models.EmailField(max_length=20)
    mobile=models.IntegerField()
    address=models.CharField(max_length=50)
    document = models.FileField(upload_to = 'patient_pic',null = True,blank = True)
    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    docs = models.ForeignKey(Docs,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patients,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.patient.name

class Prescription(models.Model):
    name = models.ForeignKey(Patients,on_delete=models.CASCADE)
    weight = models.DecimalField(decimal_places=2,max_digits=5)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name.name

class Room(models.Model):
    patient=models.ForeignKey(Patients,on_delete=models.CASCADE)
    room_taken = models.BooleanField(default=False)
    days = models.IntegerField()

    def __str__(self):
        return self.patient.name
