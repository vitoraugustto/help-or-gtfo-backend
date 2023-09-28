from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CompletedExpeditionUser


class CompletedExpeditionUserAdmin(admin.ModelAdmin):
    list_display = ("user", "expedition")


class CompletedExpeditionsInline(admin.TabularInline):
    verbose_name = "Completed expedition"
    verbose_name_plural = "Completed expeditions"
    model = CompletedExpeditionUser
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    inlines = [CompletedExpeditionsInline]
    list_display = ("username", "email", "xp", "is_active", "is_staff", "is_superuser")
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ("email",)
    ordering = ("email",)
    readonly_fields = ("date_joined", "last_login")

    fieldsets = (
        ("Basic information", {"fields": ("username", "email", "password")}),
        ("Complex", {"fields": ("xp",)}),
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
                "fields": ("email", "password1", "password2"),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CompletedExpeditionUser, CompletedExpeditionUserAdmin)
