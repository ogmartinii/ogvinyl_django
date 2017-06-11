from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^records/$', views.record_list, name='record_list'),
    url(r'^record/(?P<id>[0-9]+)/$', views.record_detail, name='record_detail'),
]