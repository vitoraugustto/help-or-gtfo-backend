from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rundown.models import Expedition
from .managers import CustomUserManager
from multiselectfield import MultiSelectField


class CompletedExpeditionUser(models.Model):
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

    def __str__(self):
        return "Completed Expedition User"


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    xp = models.PositiveIntegerField(
        null=False, blank=False, default=0, verbose_name="Experience"
    )

    completed_expeditions = models.ManyToManyField(
        Expedition,
        default=None,
        through=CompletedExpeditionUser,
        verbose_name="Completed expeditions",
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("Prisoner")
        verbose_name_plural = _("Prisoners")
