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
    ocoba = models.ForeignKey(ServiseID, on_delete=models.CASCADE, blank=True, verbose_name= _('ocoba'), null=True)
    vos = models.CharField(max_length=512, verbose_name= _('VOS'))
    poz = models.CharField(max_length=512, verbose_name= _('pozyvnyy'), blank=True)
    salary = models.PositiveBigIntegerField(verbose_name= _('salary'), blank=True)
    tariff_category = models.PositiveBigIntegerField(verbose_name= _('tariff category'), blank=True)
    vacant = models.BooleanField(verbose_name= _('Vacant'), blank=True, null=True, default=True)

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Staff')
        verbose_name_plural = _('Staff')

