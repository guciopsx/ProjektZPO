from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    character = models.ForeignKey('DjangoRpg.Chara', on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Map(models.Model):
    x = models.IntegerField(max_length=10)
    y = models.IntegerField(max_length=10)
    n = models.IntegerField(max_length=10)
    w = models.IntegerField(max_length=10)
    e = models.IntegerField(max_length=10)
    s = models.IntegerField(max_length=10)
    type = models.CharField(max_length=30)
    enemy = models.IntegerField(max_length=30, default=None, null=True)
    chest = models.IntegerField(max_length=30, default=None, null=True)

    def __str__(self):
        return self.type
    def __int__(self):
        return self.x

    def __int__(self):
        return self.y

    def __int__(self):
        return self.n

    def __int__(self):
        return self.w

    def __int__(self):
        return self.e

    def __int__(self):
        return self.s

class Chara(models.Model):
    charname = models.CharField
    race = models.IntegerField
    level = models.IntegerField
    hp = models.IntegerField
    mp = models.IntegerField
    attack = models.IntegerField
    mattack = models.IntegerField
    defence = models.IntegerField
    mapcell = models.ForeignKey('DjangoRpg.Map', on_delete=models.CASCADE)
