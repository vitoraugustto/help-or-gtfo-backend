from django.contrib import admin
from .models import Rundown, Expedition

class ExpeditionInline(admin.TabularInline):
    model = Expedition
    extra = 0

class RundownAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'release_date')
    inlines = [ExpeditionInline]

class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'rundown')

admin.site.register(Rundown, RundownAdmin)
admin.site.register(Expedition, ExpeditionAdmin)
