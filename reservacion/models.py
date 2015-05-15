from django.db import models
from concierto_zona.models import Concierto_Zona
from zona.models import Zona



class Reservacion(models.Model):
	concierto_z = models.ForeignKey(Concierto_Zona)
	lugar = models.BigIntegerField(null = True)
	def __unicode__(self):
		return str(self.concierto.descripcion)