from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OsobaConfig(AppConfig):
    name = 'osoba'
    verbose_name = _("Persons")
