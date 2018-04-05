from django.http import HttpResponse
from django.shortcuts import loader


def index(request):
    template = loader.get_template('curr_res/base_curr_res.html')
    return HttpResponse(template.render(request))
