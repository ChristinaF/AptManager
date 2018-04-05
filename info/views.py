from django.http import HttpResponse
from django.shortcuts import loader
from .models import OfficeStaff


def index(request):
    office_staff = OfficeStaff.objects.all()
    template = loader.get_template('info/base_info.html')
    return HttpResponse(template.render({'office_staff': office_staff}, request))



def detail(request, staff_id):
    member = OfficeStaff.objects.get(pk=staff_id)
    template = loader.get_template('info/detail.html')
    return HttpResponse(template.render({'member': member}, request))
