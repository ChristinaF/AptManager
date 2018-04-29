"""AptManager URL Configuration

"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    url(r'', include('homepage.urls', namespace='home')),
    #url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^curr_res/', include('curr_res.urls', namespace='curr_res')),
    url(r'^info/', include('info.urls', namespace='info')),
    url(r'^prosp_res/', include('prosp_res.urls', namespace='prosp_res')),
]
