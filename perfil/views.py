# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404,render
from django.template import RequestContext
from django.views.generic import TemplateView, RedirectView, FormView,DetailView

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
class LoginView(FormView):
	form_class = AuthenticationForm#Esto ya esta definido en el django
	template_name = 'index.html'
	success_url = '/reservacion/'

	def form_valid(self, form):
		login(self.request, form.user_cache)#Lo hace automaticamente
		return super(LoginView, self).form_valid(form)


    #Retorna los valores al template como nuevas variables
	def get_context_data(self, **kwargs):
		context = super(LoginView, self).get_context_data(**kwargs)
		
		#context.update(data)
		return context