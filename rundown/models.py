from django.db import models
from multiselectfield import MultiSelectField


class TiersXP:
    A = 10
    B = 30
    C = 50
    D = 75
    E = 100


class Rundown(models.Model):
    title = models.CharField(
        blank=False, null=False, max_length=20, verbose_name="Title"
    )
    number = models.PositiveIntegerField(blank=False, null=False, verbose_name="Number")
    release_date = models.DateField(
        blank=False, null=False, verbose_name="Release date"
    )

    class Meta:
        verbose_name = "Rundown"
        verbose_name_plural = "Rundowns"
        ordering = ["number"]

    def __str__(self):
        return f"ALT://RUNDOWN {self.number}.0"


class Expedition(models.Model):
    TIERS = [
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E"),
    ]

    DIFFICULTIES = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("X", "X")]

    display_name = models.CharField(
        blank=False, null=False, max_length=4, verbose_name="Display name"
    )
    title = models.CharField(
        blank=False, null=False, max_length=20, verbose_name="Title"
    )
    tier = models.CharField(
        blank=False, null=False, max_length=1, choices=TIERS, verbose_name="Tier"
    )
    difficulty = models.CharField(
        blank=False,
        null=False,
        max_length=1,
        choices=DIFFICULTIES,
        verbose_name="Difficulty",
    )
    rundown = models.ForeignKey(
        Rundown,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Rundown",
    )
    main_sector = models.BooleanField(default=True, verbose_name="Main")
    secondary_sector = models.BooleanField(default=False, verbose_name="Secondary")
    overload_sector = models.BooleanField(default=False, verbose_name="Overload")
    xp = models.PositiveIntegerField(null=False, blank=False, verbose_name="Experience")

    class Meta:
        verbose_name = "Expedition"
        verbose_name_plural = "Expeditions"

    def __str__(self):
        return self.display_name

    def save(self, *args, **kwargs):
        tier_xp_mapping = {
            "A": TiersXP.A,
            "B": TiersXP.B,
            "C": TiersXP.C,
            "D": TiersXP.D,
            "E": TiersXP.E,
        }

        self.display_name = f"R{self.rundown.number}{self.tier}{self.difficulty}"
        self.xp = tier_xp_mapping.get(self.tier, 0)

        super(Expedition, self).save(*args, **kwargs)
