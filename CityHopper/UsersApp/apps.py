from django.apps import AppConfig


class UsersappConfig(AppConfig):
    name = 'UsersApp'

    def ready(self):
        import UsersApp.signals
