from django.apps import AppConfig


class CustomUserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"

    def ready(self):
        import user.signals
