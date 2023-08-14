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