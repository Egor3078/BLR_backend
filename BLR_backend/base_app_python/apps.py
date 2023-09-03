from django.apps import AppConfig


class BaseAppPythonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_app_python'
