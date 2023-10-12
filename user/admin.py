from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CompletedExpeditions, CustomUser


class CompletedExpeditionsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "expedition",
        "cleared_main_sector",
        "cleared_secondary_sector",
        "cleared_overload_sector",
        "prisoner_efficiency",
        "completed_at",
    )

    readonly_fields = (
        "cleared_main_sector",
        "completed_at",
    )

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "expedition",
                ),
            },
        ),
        ("Dates", {"fields": ("completed_at",)}),
        (
            "Cleared Sectors",
            {
                "fields": (
                    "cleared_main_sector",
                    "cleared_secondary_sector",
                    "cleared_overload_sector",
                )
            },
        ),
    )


class CompletedExpeditionsInline(admin.TabularInline):
    verbose_name = "Completed expedition"
    verbose_name_plural = "Completed expeditions"
    model = CompletedExpeditions
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    inlines = [CompletedExpeditionsInline]
    list_display = ("username", "email", "level", "xp")
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ("email",)
    ordering = ("email",)
    readonly_fields = ("date_joined", "last_login", "level")

    fieldsets = (
        ("Basic information", {"fields": ("username", "email", "password")}),
        (
            "Complex",
            {
                "fields": (
                    "level",
                    "xp",
                )
            },
        ),
        ("Dates", {"fields": ("last_login", "date_joined")}),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "user_permissions")},
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CompletedExpeditions, CompletedExpeditionsAdmin)
