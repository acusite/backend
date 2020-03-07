from django.db import models
from events.models import Event
from profiles.models import Profile

# Create your models here.


class RegistrationManager(models.Manager):
    def create(self, event, player):
        instance = self.model(
            event=event,
            player=player
        )
        instance.save()
        return instance


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    player = models.ForeignKey(Profile, on_delete=models.CASCADE)

    objects = RegistrationManager()
