from django.urls import path
from .views import (
    RegistrationsListAPIView,
    RegisterAPIView,
    RegisteredListAPIView,
    NotYetPlayedListAPIView,
    PlayedListAPIView,
)


urlpatterns = [
    path('', RegistrationsListAPIView.as_view(), name='registrations_list'),
    path('register/', RegisterAPIView.as_view(), name='registration'),
    path('registered/', RegisteredListAPIView.as_view(), name='registered_events'),
    path('notplayed/', NotYetPlayedListAPIView.as_view(), name='not_yet_played_list'),
    path('played/<str:slug>/', PlayedListAPIView.as_view(), name='played'),
]
