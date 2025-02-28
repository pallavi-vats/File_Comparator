from django.apps import AppConfig


class FileCompareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'file_compare'
    
    def ready(self):
        import file_compare.signals
