from django.http import HttpResponse
from django.shortcuts import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render
from .forms import UserForm
from .models import Tenant, Apartment, Payment


def index(request):
    template = loader.get_template('curr_res/base_curr_res.html')
    return HttpResponse(template.render(request))


def logout(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'curr_res/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'curr_res/curr_res_home.html')
            else:
                return render(request, 'curr_res/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'curr_res/login.html', {'error_message': 'Invalid login'})
    return render(request, 'curr_res/login.html')


def info(request):
    if not request.user.is_authenticated():
        return render(request, 'curr_res/login.html')
    else:
        template = loader.get_template('curr_res/info.html')
        return HttpResponse(template.render(request))



def payment(request):
    template = loader.get_template('curr_res/payment.html')
    return HttpResponse(template.render(request))


def resident_home(request):
    template = loader.get_template('curr_res/curr_res_home.html')
    return HttpResponse(template.render(request))