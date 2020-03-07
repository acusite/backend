from rest_framework.generics import ListAPIView
from .serializers import RegistrationListSerializer
from .models import Registration
from events.models import Event

# Create your views here.


class RegistrationListAPIView(ListAPIView):
    serializer_class = RegistrationListSerializer
    queryset = Registration.objects.all()

    def get_queryset(self):
        event = Event.objects.get(slug=self.request.GET.get("slug"))
        return Registration.objects.filter(event=event)
