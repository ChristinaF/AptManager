from django.http import HttpResponse
from django.shortcuts import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render
from .forms import UserForm
from .models import Tenant


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


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                tenants = Tenant.objects.filter(user=request.user)
                return render(request, 'curr_res/base_curr_res.html', {'tenants': tenants})
            else:
                return render(request, 'curr_res/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'curr_res/login.html', {'error_message': 'Invalid login'})
    return render(request, 'curr_res/login.html')
