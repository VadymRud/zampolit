from django.db import models
from osoba.models import ServiseID, Company
from django.utils.translation import gettext as _


class SHPK(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('SHPK')
        verbose_name_plural = _('SHPK')


class Staff(models.Model):
    # Штатка
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, verbose_name= _('Company'))
    name = models.CharField(max_length=512, verbose_name=_('Name'))
    shpk = models.ForeignKey(SHPK, on_delete=models.CASCADE, blank=True, verbose_name= _('shpk'))
    ocoba = models.ForeignKey(ServiseID, on_delete=models.CASCADE, blank=True, verbose_name= _('ocoba'))
    vos = models.CharField(max_length=512, verbose_name= _('VOS'))
    salary = models.PositiveBigIntegerField(verbose_name= _('salary'))
    tariff_category = models.PositiveBigIntegerField(verbose_name= _('tariff category'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Staff')
        verbose_name_plural = _('Staff')

