from django.urls import path
from .views import TeamMembersListAPIView, EventListAPIView, AddMemberAPIView


urlpatterns = [
    path('', EventListAPIView.as_view(), name='event_list'),
    path('members/', TeamMembersListAPIView.as_view(), name='Team_members'),
    path('add/', AddMemberAPIView.as_view(), name='Add_Team_member'),
]
