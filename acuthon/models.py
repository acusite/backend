from django.db import models
from events.models import Event
from profiles.models import generate_id

# Create your models here.


class AcuthonRegisterManager(models.Manager):
    def create_leader(self, event, member, contact, rollnumber, email):
        instance = self.model(
            event=event,
            member=member,
            contact=contact,
            email=email,
            rollnumber=rollnumber,
        )
        instance.team_leader = True
        instance.save()
        return instance

    def create(self, event, member, rollnumber):
        instance = self.model(
            event=event,
            member=member,
            rollnumber=rollnumber,
        )
        instance.save()
        return instance


class AcuthonRegister(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.CharField(max_length=255)
    team_leader = models.BooleanField(default=False)
    contact = models.CharField(max_length=10, default=' ')
    rollnumber = models.CharField(max_length=20, default='No rollnumber given')
    email = models.EmailField(default='acumenmember@vce.com')
    slug = models.SlugField(max_length=8, default=generate_id)

    objects = AcuthonRegisterManager()
