from django.db import models
from events.models import Event
from profiles.models import Profile
from profiles.models import generate_id

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
    slug = models.SlugField(default=generate_id)
    played = models.BooleanField(default=False)

    objects = RegistrationManager()

    def __str__(self):
        return f"{self.player.username} has registered for event {self.event.name} -- { 'played' if self.played else 'not yet played'}"
