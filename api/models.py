from django.db import models
from geoposition.fields import GeopositionField

class Event(models.Model):
	owner = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=255)
	event_type = models.CharField('Type', max_length=30)
	date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)
	position = GeopositionField()
		 
	class Meta:
		verbose_name_plural = 'Eventos'
