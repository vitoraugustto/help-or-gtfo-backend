from django.contrib import admin
from .models import Prisoner
from django.contrib.auth.admin import UserAdmin

admin.site.register(Prisoner, UserAdmin)