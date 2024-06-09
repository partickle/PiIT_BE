from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Event
        fields = ['id', 'title', 'content', 'created_at', 'user', 'event_date']
