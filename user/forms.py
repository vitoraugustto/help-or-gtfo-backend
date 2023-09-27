from django import forms
from .models import CompletedExpeditionUser


class CompletedExpeditionUserForm(forms.ModelForm):
    class Meta:
        model = CompletedExpeditionUser
        fields = ["user", "expedition", "cleared_sectors"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get("instance")
        if instance and instance.expedition:
            sector_choices = instance.expedition.get_sector_choices()

            self.fields["cleared_sectors"].choices = sector_choices
