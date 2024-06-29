from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self):
        # Your app-specific code that relies on loaded apps
        # This code will run after the app is fully loaded
        pass
