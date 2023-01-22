from django.db import models
import datetime

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=64)
    field=models.CharField(max_length=64)

    def __str__(self):
        return f"Doctor{self.name} ({self.field})"

class Patient(models.Model):
    name=models.CharField(max_length=64)
    address=models.CharField(max_length=64)
    age=models.IntegerField(default=0)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name};\n Address: {self.address};\n Age: {self.age}"

class Confirmation(models.Model):
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctor")
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient")
    time=models.DateTimeField()
    number=models.IntegerField(default=0)
    
    def __str__(self):
        return f"Confirmation number {self.number}: {self.patient} with Dr. {self.doctor} at {self.time}"

    


 

