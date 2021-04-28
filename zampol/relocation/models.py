from django.db import models
from osoba.models import ServiseID
from staff.models import Staff
from django.utils.translation import gettext as _
# Create your models here.


class Relocation(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'), blank=True)
    from_staff = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, verbose_name= _('from staff'),
                                   related_name = 'fromstaff')
    to_staff = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, verbose_name=_('to staff'),
                                   related_name='tostaff')
    order_number = models.CharField(max_length=512, verbose_name=_('order number'))
    order_date = models.DateField(verbose_name=_('order date'))
    appruve = models.BooleanField(verbose_name=_('order number'))
    appruve_date = models.DateField(verbose_name=_('appruve date'))
    osoba = models.ForeignKey(ServiseID, on_delete=models.CASCADE, verbose_name= _('osoba'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Relocation')
        verbose_name_plural = _('Relocation\'s')
