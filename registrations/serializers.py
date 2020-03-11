from rest_framework import serializers
from .models import Registration
from events.models import Event
from profiles.models import Profile


class RegistrationsListSerializer(serializers.ModelSerializer):
    eventName = serializers.SerializerMethodField()
    playerName = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = [
            'eventName',
            'playerName',
        ]

    def get_eventName(self, obj):
        return str(obj.event.name)

    def get_playerName(self, obj):
        return str(obj.player.username)


class RegisterSerializer(serializers.ModelSerializer):
    eventName = serializers.SerializerMethodField()
    playerName = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = [
            'eventName',
            'playerName',
            'event',
            'player',
        ]

    def create(self, validated_data):
        event = Event.objects.get(slug=self.context.get('request').GET.get('event'))
        return Registration.objects.create(event=event, player=self.context.get('request').user)

    def get_eventName(self, obj):
        return str(obj.event.name)

    def get_playerName(self, obj):
        return str(obj.player.username)


class RegisteredListSerializer(serializers.ModelSerializer):
    eventName = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = [
            'eventName',
        ]

    def get_eventName(self, obj):
        return str(obj.event.name)