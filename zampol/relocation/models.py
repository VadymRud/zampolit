from django.db import models
from osoba.models import ServiseID
from django.utils.translation import gettext as _
# Create your models here.


class Relocation(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Relocation')
        verbose_name_plural = _('Relocation\'s')
