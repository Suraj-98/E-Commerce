from django.apps import AppConfig


class e_shopperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'e_shopper'

    def ready(self):
        import e_shopper.signals
