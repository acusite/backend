from django.db import models
import string as str
from random import choice


# Create your models here.


def generate_id():
    n = 8
    random = str.ascii_uppercase + str.ascii_lowercase + str.digits + '_'
    return ''.join(choice(random) for _ in range(n))


class AcuthonManager(models.Manager):
    def create(self, name):
        instance = self.model(
            name=name,
        )
        instance.save()
        return instance


class Acuthon(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False, default=generate_id)
    slug = models.SlugField(max_length=100, unique=True, default=generate_id)

    objects = AcuthonManager()


class AcuthonRegisterManager(models.Manager):
    def create_leader(self, team, member, contact, rollnumber, email):
        instance = self.model(
            team=team,
            member=member,
            contact=contact,
            email=email,
            rollnumber=rollnumber,
        )
        instance.team_leader = True
        instance.save()
        return instance

    def create(self, team, member, rollnumber):
        instance = self.model(
            team=team,
            member=member,
            rollnumber=rollnumber,
        )
        instance.save()
        return instance


class AcuthonRegister(models.Model):
    team = models.ForeignKey(Acuthon, on_delete=models.CASCADE, related_name='Acuthon', null=True)
    member = models.CharField(max_length=255)
    team_leader = models.BooleanField(default=False)
    contact = models.CharField(max_length=10, default=' ')
    rollnumber = models.CharField(max_length=20, default='No rollnumber given')
    email = models.EmailField(default='acumenmember@vce.com')
    slug = models.SlugField(max_length=8, unique=True, default=generate_id)

    objects = AcuthonRegisterManager()
