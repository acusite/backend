from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models import Q
import string as str
from random import choice

# Create your models here.
I = 'I'
II = 'II'
III = 'III'
IV = 'IV'


YEAR_CHOICES = ((I, 'I'), (II, 'II'), (III, 'III'), (IV, 'IV'))

IT = 'IT'
EEE = 'EEE'
ECE = 'ECE'
CIVIL = 'CIVIL'
CSE = 'CSE'
MECH = 'MECH'
CHEMICAL = 'CHEMICAL'
EIE = 'EIE'
TEXTILE = 'TEXTILE'

BRANCH_CHOICES = ((IT, 'INFORMATION TECHNOLOGY'), (EEE, 'ELECTRICAL AND ELECTRONICS ENGINEERING'),
                  (ECE, 'ELECTRONICS AND COMMUNICATION ENGINEERING'), (CIVIL, 'CIVIL'), (CSE, 'COMPUTER SCIENCE'),
                  (MECH, 'MECHANICAL'), (CHEMICAL, 'CHEMICAL'),
                  (EIE, 'ELECTRONICS AND INSTRUMENTATION ENGINEERING'), (TEXTILE, 'TEXTILE'))


def generate_id():
    n = 8
    random = str.ascii_uppercase + str.ascii_lowercase + str.digits + '_'
    return ''.join(choice(random) for _ in range(n))


def generate_email():
    n = 4
    random = str.digits
    st = ''.join(choice(random) for _ in range(n))
    return 'acumen'+st+'@gmail.com'


class ProfileQueryset(models.QuerySet):

    def search(self, query):
        lookup = (
            Q(username__icontains=query) |
            Q(email_id__icontains=query) |
            Q(contact__icontains=query)
        )
        return self.filter(lookup)


class ProfileManager(BaseUserManager):
    def get_queryset(self):
        return ProfileQueryset(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)

    def create_user(self, username, password, email_id, roll_number, department, year, contact):
        q = Profile.objects.filter(username=username)
        if q.exists():
            raise ValueError("username already been taken")
        user = self.model(
            username=username.casefold(),
            email_id=self.normalize_email(email_id).casefold(),
            roll_number=roll_number,
            department=department,
            year=year,
            contact=contact,
        )
        user.is_admin = False
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self, username, email_id, roll_number, contact, password):
        if not username:
            raise ValueError('Username is required')

        if not email_id:
            raise ValueError('Email is required')

        q = Profile.objects.filter(username=username)
        if q.exists():
            raise ValueError("username already been taken")
        user = self.model(
            username=username.casefold(),
            email_id=self.normalize_email(email_id).casefold(),
            roll_number=roll_number,
            contact=contact,
        )
        user.is_admin = True
        user.year = 'IV'
        user.set_password(password)
        user.save(using=self._db)


class Profile(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=255, null=False, blank=False)
    profile_unique_key = models.CharField(max_length=8, unique=True, default=generate_id)
    email_id = models.EmailField(unique=True, null=False, blank=False, default=generate_email)
    roll_number = models.CharField(max_length=255, blank=False, null=False, default='Not interested')
    department = models.CharField(max_length=100, choices=BRANCH_CHOICES, default='IT')
    year = models.CharField(max_length=3, choices=YEAR_CHOICES, default='I')
    contact = models.CharField(max_length=10, null=False, blank=False, default='No Number')
    is_admin = models.BooleanField(default=False)

    objects = ProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email_id', 'roll_number', 'contact', ]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, profiles):
        return True

    @property
    def is_staff(self):
        return self.is_admin
