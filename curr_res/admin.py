from django.contrib import admin
from .models import Tenant, Apartment, Payment


# Register your models here.


admin.site.register(Tenant)
admin.site.register(Apartment)
admin.site.register(Payment)
