from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil (models.Model):
	user = models.OneToOneField(User, unique=True, related_name='perfil')
	telefono = models.CharField(max_length=300, blank=True,null = True)

	def __unicode__(self):
		return self.user.first_name 