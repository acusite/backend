from django.urls import path
from .views import LikeAPIView, LikesListAPIView


urlpatterns = [
    path('like/', LikeAPIView.as_view(), name='like_event'),
    path('likeson/', LikesListAPIView.as_view(), name='likes_on_event'),
]