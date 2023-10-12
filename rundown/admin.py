from django.contrib import admin

from .models import Expedition, Rundown


class ExpeditionInline(admin.TabularInline):
    readonly_fields = ("xp",)
    model = Expedition
    extra = 0


class RundownAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title", "release_date")
    inlines = [ExpeditionInline]


class ExpeditionAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "title",
        "main_sector",
        "secondary_sector",
        "overload_sector",
        "rundown",
    )
    readonly_fields = ("main_sector",)
    exclude = ("display_name", "xp")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "tier",
                    "difficulty",
                    "rundown",
                )
            },
        ),
        (
            "Sectors",
            {
                "fields": (
                    "main_sector",
                    "secondary_sector",
                    "overload_sector",
                )
            },
        ),
    )


admin.site.register(Rundown, RundownAdmin)
admin.site.register(Expedition, ExpeditionAdmin)
