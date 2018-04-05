from django.http import HttpResponse
from django.shortcuts import loader


def index(request):
    template = loader.get_template('prosp_res/base_prosp_res.html')
    return HttpResponse(template.render(request))
