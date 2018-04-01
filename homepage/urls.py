from django.conf.urls import url
from . import views


urlpatterns = [
    # /info/
    url(r'^$', views.index, name='index'),
    ]