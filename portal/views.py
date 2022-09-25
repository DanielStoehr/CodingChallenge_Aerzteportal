from django.shortcuts import render
from rest_framework import viewsets, mixins
from portal.models import Appointment, Doctor, Patient
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.filter(
            Q(patient__user=self.request.user) | Q(doctor__user=self.request.user)
        )
