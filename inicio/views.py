# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404,render
from django.template import RequestContext
from django.http import  HttpResponseRedirect
from django.views.generic import View,TemplateView, RedirectView, FormView

#from menu.models import Menu
class ClassView(View):
    def get(self, request):
    	if not request.user.is_authenticated():
    		return HttpResponseRedirect('/login/')
    	else:
    		return HttpResponseRedirect('/reservacion/')	