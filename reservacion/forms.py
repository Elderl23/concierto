from django import forms
from django.forms import ModelForm

from .models import Reservacion

class FormReservacion(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ('concierto_z',)
