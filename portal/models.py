from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Doctor_Speciality(models.Model):
    speciality = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.speciality


class Doctor_Title(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class Doctor(models.Model):
    speciality = models.ForeignKey(Doctor_Speciality, on_delete=models.CASCADE)
    title = models.ForeignKey(Doctor_Title, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username}, {self.title}, {self.speciality}"


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Appointment(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
