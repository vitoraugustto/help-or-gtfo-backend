from django.db import models

class Rundown(models.Model):
    title = models.CharField(blank=False, null=False, max_length=20, verbose_name='Title')
    number = models.PositiveIntegerField(blank=False, null=False, verbose_name='Number')
    release_date = models.DateField(blank=False, null=False, verbose_name='Release date')

    class Meta:
        verbose_name = 'Rundown'
        verbose_name_plural = 'Rundowns'
        ordering = ['number']

    def __str__(self):
        return f'ALT://RUNDOWN {self.number}.0'

class Expeditions(models.Model):
    TIERS = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]

    DIFFICULTIES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('X', 'X')
    ]

    title = models.CharField(blank=False, null=False, max_length=20, verbose_name='Title')
    tier = models.CharField(blank=False, null=False, max_length=1, choices=TIERS, verbose_name='Tiers')
    difficulty = models.CharField(blank=False, null=False, max_length=1, choices=DIFFICULTIES, verbose_name='Difficulty') 
    rundown = models.ForeignKey(Rundown, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Rundown')

    class Meta:
        verbose_name = 'Expedition'
        verbose_name_plural = 'Expeditions'

    def __str__(self):
        return f'R{self.rundown.number}{self.tier}{self.difficulty}'