from django import forms
from django.contrib.auth.models import User
from .models import ClubhouseReservation



class ReservationForm(forms.ModelForm):

    class Meta:
        model = ClubhouseReservation
        fields = ['tenant_name', 'date', 'time', 'event']
