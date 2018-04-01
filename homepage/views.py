from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import loader


def index(request):
    template = loader.get_template('homepage/base_homepage.html')
    return HttpResponse(template.render(request))