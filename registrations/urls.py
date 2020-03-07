from django.urls import path
from .views import RegistrationListAPIView


urlpatterns = [
    path('', RegistrationListAPIView.as_view(), name='registrations_list'),
]
