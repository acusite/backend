from rest_framework import serializers
from .models import EventMember, Event
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class EventMemberListSerializer(serializers.ModelSerializer):
    event = serializers.SerializerMethodField()
    member = serializers.SerializerMethodField()

    class Meta:
        model = EventMember
        fields = [
            'event',
            'member',
        ]

    def get_member(self, obj):
        return str(obj.member.username)

    def get_event(self, obj):
        return str(obj.event.name)


class EventListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'name',
            'description',
            'slug',
        ]


class CreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventMember
        fields = [
            'event',
            'member',
        ]

    def create(self, validated_data):
        slug = self.context.get("slug")
        request = self.context.get("request")
        event = Event.objects.get(slug=slug)
        qs = EventMember.objects.filter(event=event, member=request.user)
        if qs.exists():
            raise ValidationError("Connection already exists")
        return EventMember.create(event=event, member=request.user)
