from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import ClassView

urlpatterns = patterns('',
    url(r'^$', ClassView.as_view(), name='ClassView'),
    #url(r'^home/$', LoginView.as_view(), name='LoginView'),

)
