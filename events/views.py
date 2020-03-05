from .serializers import EventMemberListSerializer, EventListSerializer, CreateSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Event, EventMember
# Create your views here.


class TeamMembersListAPIView(ListAPIView):
    serializer_class = EventMemberListSerializer

    def get_queryset(self):
        slug = self.request.GET.get("event")
        event = Event.objects.get(slug=slug)
        return EventMember.objects.filter(event=event)

    class Meta:
        model = EventMember


class EventListAPIView(ListAPIView):
    serializer_class = EventListSerializer
    queryset = Event.objects.all()

    class Meta:
        model = Event


class AddMemberAPIView(CreateAPIView):
    serializer_class = CreateSerializer
    queryset = EventMember.objects.all()

    def get_serializer_context(self):
        context = {'request': self.request, 'slug': self.request.GET.get("slug")}
        return context
