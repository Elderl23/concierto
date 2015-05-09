from django.db import models

class Tiempo(models.Model):
	maximo = models.BigIntegerField(null = True)
	def __unicode__(self):
		return str(self.maximo)