from django.forms import ModelForm
from django import forms
from api.models import Event

class EventForm(ModelForm):
	name = forms.CharField(
		label='Nome:',
		required = True,
	)
	description = forms.CharField(
		label='Descrição:',
		required = True,
	)
	event_type = forms.CharField(
		label='Descrição:',
		required = True,
	)
	class Meta:
		model = Event
		fields = ['name', 'description','event_type','position']