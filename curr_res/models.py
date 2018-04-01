from django.db import models

# Create your models here.


class Tenant(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    apt_address = models.CharField(max_length=30)
    apt_city = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)

    def _str_(self):
        return self.first_name + "\n" + self.last_name