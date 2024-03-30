from django.apps import AppConfig


class LimitedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'limited'
    verbose_name = '地区不可再生能源'
