from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^info', views.info, name='info'),
    url(r'^payment', views.payment, name='payment'),
    url(r'^resident_home', views.resident_home, name='resident_home')
]