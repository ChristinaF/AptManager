"""AptManager URL Configuration

"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^curr_res/', include('curr_res.urls')),
    url(r'^info/', include('info.urls')),
    url(r'^homepage/', include('homepage.urls')),
    url(r'^prosp_res/', include('prosp_res.urls')),
]
