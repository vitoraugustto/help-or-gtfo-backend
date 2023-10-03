import math

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rundown.models import Expedition
from .managers import CustomUserManager
from multiselectfield import MultiSelectField


class CompletedExpeditions(models.Model):
    user = models.ForeignKey(
        "CustomUser",
        null=False,
        blank=False,
        verbose_name="User",
        on_delete=models.CASCADE,
    )
    expedition = models.ForeignKey(
        Expedition,
        null=False,
        blank=False,
        verbose_name="Expedition",
        on_delete=models.CASCADE,
    )
    cleared_main_sector = models.BooleanField(default=True, verbose_name="Main")
    cleared_secondary_sector = models.BooleanField(
        default=False, verbose_name="Secondary"
    )
    cleared_overload_sector = models.BooleanField(
        default=False, verbose_name="Overload"
    )
    prisoner_efficiency = models.BooleanField(
        default=False, verbose_name="Prisoner efficiency"
    )
    completed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Completed Expedition"

    class Meta:
        verbose_name = _("Completed expedition")
        verbose_name_plural = _("Completed expeditions")

    def save(self, *args, **kwargs):
        if (
            self.cleared_main_sector
            and self.cleared_secondary_sector
            and self.cleared_overload_sector
        ):
            self.prisoner_efficiency = True

        super(CompletedExpeditions, self).save(*args, **kwargs)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True, blank=True)
    username = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    level = models.PositiveIntegerField(
        null=False, blank=False, default=0, verbose_name="Level"
    )
    xp = models.PositiveIntegerField(
        null=False, blank=False, default=0, verbose_name="Experience"
    )
    completed_expeditions = models.ManyToManyField(
        Expedition,
        default=None,
        through=CompletedExpeditions,
        verbose_name="Completed expeditions",
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def calculate_level(self):
        scaling_factor = 10

        level = math.floor(math.sqrt(self.xp / scaling_factor))
        self.level = level

    class Meta:
        verbose_name = _("Prisoner")
        verbose_name_plural = _("Prisoners")

    def save(self, *args, **kwargs):
        self.calculate_level()

        super(CustomUser, self).save(*args, **kwargs)
