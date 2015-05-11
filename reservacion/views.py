# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404,render
from django.template import RequestContext

from django.views.generic import TemplateView, RedirectView, FormView

from zona.models import Zona
class ReservacionView(TemplateView):
    #template_name = 'index.html'
    template_name = 'ventas.html'
    #template_name = 'confirmar-ventas.html'

    def post(request, *args, **kwargs):
		ObjQueryZona = Zona.objects.all()
		data = {
			'ObjQueryZona':ObjQueryZona,
		}
		context.update(data)

    #Retorna los valores al template como nuevas variables
    def get_context_data(self, **kwargs):
		context = super(ReservacionView, self).get_context_data(**kwargs)
		ObjQueryZona = Zona.objects.all()

		data = {
			'ObjQueryZona':ObjQueryZona,
		}

		context.update(data)
		return context		
