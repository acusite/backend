from rest_framework.generics import CreateAPIView
from .serializers import AcuthonRegisterSerializer, TeamRegisterSerializer
from .models import AcuthonRegister, Acuthon

# Create your views here.


class TeamRegisterAPIView(CreateAPIView):
    serializer_class = TeamRegisterSerializer
    queryset = Acuthon.objects.all()

    class Meta:
        model = Acuthon


class AcuthonRegisterAPIView(CreateAPIView):
    serializer_class = AcuthonRegisterSerializer
    queryset = AcuthonRegister.objects.all()

    class Meta:
        model = AcuthonRegister

    def get_serializer_context(self):
        return {'team': self.request.GET.get('team')}
