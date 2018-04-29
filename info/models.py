from django.db import models


class OfficeStaff(models.Model):
    class Meta:
        verbose_name = 'Office Staff'
        verbose_name_plural = 'Office Staff Members'
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return self.name + "\n" + self.role


class MaintenanceStaff(models.Model):
    class Meta:
        verbose_name = 'Maintenance Staff'
        verbose_name_plural = 'Maintenance Staff Members'
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.name + "     " + self.role

class ClubhouseReservation(models.Model):
    tenant_name = models.CharField(max_length=30)
    date = models.DateField()
    time = models.IntegerField()
    event = models.CharField(max_length=150)

    def __str__(self):
        return str(self.date) + "   " + self.tenant_name



