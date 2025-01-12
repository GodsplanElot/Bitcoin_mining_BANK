from django.apps import AppConfig

class UserAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Ensures the default primary key is a BigAutoField
    name = 'UserApp'  # This is the name of your app

    def ready(self):
        import UserApp.signals  # Import the signals module when the app is ready
