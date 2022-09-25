from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Doctor(models.Model):
    speciality = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Appointment(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
