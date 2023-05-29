from django.apps import AppConfig


class AccountConfig(AppConfig):
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField',
    name = 'account'
    verbose_name='بخش حساب کاربری'