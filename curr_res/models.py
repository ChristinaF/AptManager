from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.


class Tenant(models.Model):
    user = models.ForeignKey(User, default=1)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + "  " + self.last_name


class Apartment(models.Model):
    tenant = models.ForeignKey(Tenant)
    unit = models.CharField(max_length=10)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    cost = models.IntegerField()

    def __str__(self):
        return self.unit


class Payment(models.Model):
    tenant = models.ForeignKey(Tenant)
    rent = models.IntegerField()
    electricity = models.IntegerField()
    gas = models.IntegerField()
    due_date = models.DateField()
    amount_paid = models.IntegerField()

    def __str__(self):
        return self.tenant.first_name + "  " + self.tenant.last_name


