from django.db import models
from profiles.models import Profile
from events.models import Event

# Create your models here.


class Like(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    liked_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
