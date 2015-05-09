from django.db import models
from conciertos.models import Concierto
from zona.models import Zona



class Concierto_Zona(models.Model):
	concierto = models.ForeignKey(Concierto)
	zona = models.ForeignKey(Zona)

	lugares = models.BigIntegerField(null = True)
	stock = models.BigIntegerField(null = True)

	precio=models.DecimalField(max_digits=19, decimal_places=2)
	def __unicode__(self):
		return str(self.concierto.descripcion)+" "+str(self.zona.descripcion) +" "+str(self.lugares) +" "+str(self.precio) 