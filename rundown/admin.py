from django.contrib import admin
from .models import Rundown

class RundownAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'release_date')

admin.site.register(Rundown, RundownAdmin)
