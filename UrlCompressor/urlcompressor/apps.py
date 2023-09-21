from django.apps import AppConfig


class UrlcompressorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'urlcompressor'

    def ready(self):
        import urlcompressor.signals




