from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Like
from .serializers import LikesCreateSerializer, LikesListSerializer

# Create your views here.


class LikeAPIView(CreateAPIView):
    serializer_class = LikesCreateSerializer
    queryset = Like.objects.all()

    def get_serializer_context(self):
        return {'slug': self.request.GET.get('event'), 'user': self.request.user}


class LikesListAPIView(ListAPIView):
    serializer_class = LikesListSerializer

    def get_queryset(self):
        return Like.objects.filter(event__slug=self.request.GET.get('event'))
