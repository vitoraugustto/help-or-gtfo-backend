from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CompletedExpeditions


@receiver(post_save, sender=CompletedExpeditions)
def add_user_xp(sender, instance, **kwargs):
    user = instance.user
    user.xp += instance.expedition.xp

    if instance.cleared_secondary_sector:
        user.xp += 20
    if instance.cleared_overload_sector:
        user.xp += 60

    user.save()


@receiver(post_delete, sender=CompletedExpeditions)
def remove_user_xp(sender, instance, **kwargs):
    user = instance.user
    user.xp -= instance.expedition.xp

    if instance.cleared_secondary_sector:
        user.xp -= 20
    if instance.cleared_overload_sector:
        user.xp -= 60

    user.save()
