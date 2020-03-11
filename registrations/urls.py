from django.urls import path
from .views import RegistrationsListAPIView, RegisterAPIView, RegisteredListAPIView


urlpatterns = [
    path('', RegistrationsListAPIView.as_view(), name='registrations_list'),
    path('register/', RegisterAPIView.as_view(), name='registration'),
    path('registered/', RegisteredListAPIView.as_view(), name='registered-_events'),
]
