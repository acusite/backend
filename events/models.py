from django.db import models
from profiles.models import Profile

# Create your models here.


def remove(string):
    return string.replace(" ", "")


class Event(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    slug = models.SlugField(default=name.replace(" ", "").casefold())


class EventMember()