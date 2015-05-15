from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import LoginView

urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view(), name='LoginView'),
)