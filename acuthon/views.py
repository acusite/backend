from rest_framework.generics import CreateAPIView
from .serializers import AcuthonRegisterSerializer
from .models import AcuthonRegister

# Create your views here.


class AcuthonRegisterAPIView(CreateAPIView):
    serializer_class = AcuthonRegisterSerializer
    queryset = AcuthonRegister.objects.all()

    class Meta:
        model = AcuthonRegister
