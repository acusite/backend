from rest_framework import serializers
from .models import Registration


class RegistrationListSerializer(serializers.ModelSerializer):
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
