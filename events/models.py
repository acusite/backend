from django.db import models
from profiles.models import Profile
from profiles.models import generate_id

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    slug = models.SlugField(default=generate_id)

    def __str__(self):
        return self.name


class EventManager(models.Manager):
    def create(self, member, event):
        instance = self.model(
            member=member,
            event=event,
        )
        instance.save()
        return instance


class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='Event')
    member = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='team_member')
    slug = models.SlugField(unique=True, default=generate_id)

    objects = EventManager()

    def __str__(self):
        return f"{self.member} is the team member of the event {self.event}"
