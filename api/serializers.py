from rest_framework import serializers
from api.models import Event


class EventSerializerModel(serializers.ModelSerializer):
	position = serializers.CharField(max_length=100)
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Event
		fields = ('id', 'name', 'owner','description', 'event_type', 'date_joined','position')
