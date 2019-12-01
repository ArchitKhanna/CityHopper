from django.apps import AppConfig

#App config for CityHopper to find the App
class UsersappConfig(AppConfig):
    name = 'UsersApp'

    #overiding an in built method to listen to signals
    def ready(self):
        import UsersApp.signals
