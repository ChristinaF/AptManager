from django import forms
from django.contrib.auth.models import User
from .models import Tenant, Payment


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']


class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ['rent', 'electricity', 'gas', 'due_date', 'amount_paid']

