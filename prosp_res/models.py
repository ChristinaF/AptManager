from django.db import models

# Create your models here.


class Tenant_prospect(models.Model):
    class Meta:
        verbose_name = 'Applicant'
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + "\n" + self.last_name