from django.apps import AppConfig


class TrfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trf'

    def ready(self) -> None:
        import trf.signals