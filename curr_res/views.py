from django.http import HttpResponse
from django.shortcuts import loader


def index(request):
    return HttpResponse("<h1>Welcome to the Tenant Portal</h1>")
