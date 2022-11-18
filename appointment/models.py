from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_name=models.CharField(max_length=64)
    patient_address=models.CharField(max_length=64)
    patient_age=models.IntegerField(default=0)
    patient_id=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.patient_name}; id={self.patient_id}; Address: {self.patient_address}; Age: {self.patient_age}"

class Doctor(models.Model):
    doctor_name=models.CharField(max_length=64)
    doctor_field=models.CharField(max_length=64)
    doctor_id=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.doctor_name} ({self.doctor_field}); id={self.doctor_id}å"

class Confirmation(models.Model):
    doctor_name=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="doctor")
    patient_name=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient")
    time=models.IntegerField(default=0)
    conf_number=models.IntegerField(default=0)
    
    def __str__(self):
        return f"Confirmation number {self.conf_number}: {self.patient_name} with Dr. {self.doctor_name} at {self.time}"

    


 

