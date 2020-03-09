from django.db import models

import string as str
from random import choice


# Create your models here.


def generate_id():
    n = 8
    random = str.ascii_uppercase + str.ascii_lowercase + str.digits + '_'
    return ''.join(choice(random) for _ in range(n))


class AcuthonManager(models.Manager):
    def create(self, name, college):
        instance = self.model(
            name=name,
            college=college,
        )
        instance.save()
        return instance


class Acuthon(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False, default=generate_id)
    college = models.CharField(max_length=30, blank=False, null=False, default="Vasavi College of Engineering")
    slug = models.SlugField(max_length=100, unique=True, default=generate_id)

    objects = AcuthonManager()

    def __str__(self):
        return str(self.name)


class AcuthonRegisterManager(models.Manager):
    def create_leader(self, team, member, contact, rollnumber, college, email):
        instance = self.model(
            team=team,
            member=member,
            contact=contact,
            email=email,
            rollnumber=rollnumber,
            college=college,
        )
        instance.team_leader = True
        instance.save()
        return instance

    def create(self, team, member, rollnumber, college):
        instance = self.model(
            team=team,
            member=member,
            rollnumber=rollnumber,
            college=college,
        )
        instance.save()
        return instance


class AcuthonRegister(models.Model):
    team = models.ForeignKey(Acuthon, on_delete=models.CASCADE, related_name='Acuthon', null=True)
    college = models.CharField(max_length=30, blank=True, null=True)
    member = models.CharField(max_length=255)
    team_leader = models.BooleanField(default=False)
    contact = models.CharField(max_length=10, default=' ')
    rollnumber = models.CharField(max_length=20, default='No rollnumber given')
    email = models.EmailField(default='acumenmember@vce.com')
    slug = models.SlugField(max_length=8, unique=True, default=generate_id)

    objects = AcuthonRegisterManager()

    def __str__(self):
        return f"{self.member} is a { 'leader' if self.team_leader else 'member'} of {self.team.name}"
