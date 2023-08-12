from django.db import models
from django.contrib.auth.models import AbstractUser

class Prisoner(AbstractUser):
    xp = models.PositiveIntegerField(null=False, blank=False, default=0, verbose_name='Experience')
