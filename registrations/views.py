from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from .serializers import (
    RegistrationsListSerializer,
    RegisterSerializer,
    RegisteredListSerializer,
    PlayedSerializer,
)
from .models import Registration
from events.models import Event, EventMember

# Create your views here.


class RegistrationsListAPIView(ListAPIView):
    serializer_class = RegistrationsListSerializer
    queryset = Registration.objects.all()

    def get_queryset(self):
        member = EventMember.objects.get(member=self.request.user)
        return Registration.objects.filter(event=member.event)


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = Registration.objects.all()

    def get_serializer_context(self):
        return {'request': self.request}


class RegisteredListAPIView(ListAPIView):
    serializer_class = RegisteredListSerializer

    def get_queryset(self):
        qs = Registration.objects.filter(player=self.request.user)
        return qs


class NotYetPlayedListAPIView(ListAPIView):
    serializer_class = RegistrationsListSerializer
    queryset = Registration.objects.all()

    def get_queryset(self):
        event = Event.objects.get(slug=self.request.GET.get("slug"))
        return Registration.objects.filter(event=event, played=False)


class PlayedListAPIView(UpdateAPIView):
    lookup_field = 'slug'
    serializer_class = PlayedSerializer
    queryset = Registration.objects.all()
