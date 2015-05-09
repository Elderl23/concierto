# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404,render
from django.template import RequestContext

from django.views.generic import TemplateView, RedirectView, FormView

#from menu.models import Menu
class InicioView(TemplateView):
    template_name = 'index.html'

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(InicioView, self).get_context_data(**kwargs)
		ObjPost = "hola"

		data = {
			'ObjPost':ObjPost,
		}

		context.update(data)
		return context	