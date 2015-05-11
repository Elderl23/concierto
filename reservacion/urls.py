from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import ReservacionView

urlpatterns = patterns('',
    url(r'^reservacion/$', ReservacionView.as_view(), name='ReservacionView'),


)
