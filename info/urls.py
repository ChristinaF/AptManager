from django.conf.urls import url
from . import views


urlpatterns = [
    # /info/
    url(r'^$', views.index, name='index'),

    # /info/32/
    url(r'^(?P<staff_id>[0-9]+)/$', views.detail, name='detail'),
]