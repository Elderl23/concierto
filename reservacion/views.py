# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404,render
from django.template import RequestContext

from django.views.generic import TemplateView, RedirectView, FormView

from zona.models import Zona
from .forms import FormReservacion

class ReservacionView(FormView):
	form_class = FormReservacion
	template_name = 'ventas.html'
	success_url = '/reservacion/'

	def post(self, request, *args, **kwargs):

		form = self.get_form()
		v_zona = request.POST['zona']
		print v_zona
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def get_context_data(self, **kwargs):
		context = super(ReservacionView, self).get_context_data(**kwargs)
		ObjQueryZona = Zona.objects.all()

		data = {
		'ObjQueryZona':ObjQueryZona,
		}

		context.update(data)
		return context		