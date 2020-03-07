from rest_framework import serializers
from .models import AcuthonRegister
from events.models import Event
from rest_framework.exceptions import ValidationError


class AcuthonRegisterSerializer(serializers.ModelSerializer):
    event_name = serializers.SerializerMethodField()

    class Meta:
        model = AcuthonRegister
        fields = [
            'event_name',
            'member',
            'email',
            'contact',
            'rollnumber',
        ]

    def create(self, validated_data):
        event, created = Event.objects.get_or_create(slug='acuthon', name='Acuthon', description='Acuthon event')
        reg = AcuthonRegister.objects.filter(event=event, member=validated_data["member"])
        if reg.exists():
            raise ValidationError("Team member already exists")
        no = AcuthonRegister.objects.filter(event=event)
        if no.exists():
            return AcuthonRegister.objects.create(
                event=event,
                member=validated_data['member'],
                rollnumber=validated_data['rollnumber'],
            )
        return AcuthonRegister.objects.create_leader(
            event=event,
            member=validated_data['member'],
            email=validated_data['email'],
            contact=validated_data['contact'],
            rollnumber=validated_data['rollnumber']
        )

    def get_event_name(self, obj):
        return str(obj.event.name)
