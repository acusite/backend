from django.urls import path
from .views import AcuthonRegisterAPIView

urlpatterns = [
    path('register/', AcuthonRegisterAPIView.as_view(), name='register_event'),
]