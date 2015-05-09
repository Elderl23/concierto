from django.db import models

class Zona(models.Model):
	descripcion = models.CharField(max_length=255)
	def __unicode__(self):
		return self.descripcion