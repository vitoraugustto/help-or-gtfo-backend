from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CompletedExpeditions


class SectorXP:
    Secondary = 40
    Overload = 80


@receiver(post_save, sender=CompletedExpeditions)
def add_user_xp(sender, instance, **kwargs):
    user = instance.user

    if instance.cleared_main_sector:
        user.xp += instance.expedition.xp
    if instance.cleared_secondary_sector:
        user.xp += SectorXP.Secondary
    if instance.cleared_overload_sector:
        user.xp += SectorXP.Overload

    user.save()


@receiver(post_delete, sender=CompletedExpeditions)
def remove_user_xp(sender, instance, **kwargs):
    user = instance.user

    if instance.cleared_main_sector:
        user.xp -= instance.expedition.xp
    if instance.cleared_secondary_sector:
        user.xp -= SectorXP.Secondary
    if instance.cleared_overload_sector:
        user.xp -= SectorXP.Overload

    user.save()
