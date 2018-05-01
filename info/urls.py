from django.conf.urls import url
from . import views


urlpatterns = [
    # /info/
    url(r'^$', views.info_main, name='info_main'),

    # /info/32/
    url(r'^(?P<staff_id>[0-9]+)/$', views.detail, name='detail'),
]