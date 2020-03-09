from django.urls import path
from .views import AcuthonRegisterAPIView, TeamRegisterAPIView

urlpatterns = [
    path('team/', TeamRegisterAPIView.as_view(), name='register_team'),
    path('register/', AcuthonRegisterAPIView.as_view(), name='register_event'),
]