from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RewardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reward'
    verbose_name = _('Rewards and Penalties')
