from django.shortcuts import render
from rest_framework import viewsets, mixins
from portal.models import Appointment, Doctor, Patient

from portal.serializers import (
    AppointmentSerializer,
    DoctorSerializer,
    PatientSerializer,
)

# Create your views here.


class DoctorViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class PatientViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class AppointmentViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
