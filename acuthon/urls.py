from django.urls import path
from .views import AcuthonRegisterAPIView, TeamRegisterAPIView, AcuthonDeleteAPIView


urlpatterns = [
    path('team/', TeamRegisterAPIView.as_view(), name='register_team'),
    path('register/', AcuthonRegisterAPIView.as_view(), name='register_event'),
    path('delete/<str:slug>/', AcuthonDeleteAPIView.as_view(), name='delete_acuthon'),
]
