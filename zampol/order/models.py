from django.db import models
from django.utils import timezone
from osoba.models import ServiseID
from staff.models import Staff
from django.utils.translation import gettext as _
# Create your models here.


class StatusOrder(models.Model):
    CHOICES = (
        ('APP', _('Appointment')),
        ('MOV', _('Moving')),
        ('RA', _('Rank')),
        ('AL', _('Annual leave')),
        ('VFR', _('Vacation for family reasons')),
        ('SZCH', _('Unauthorized leaving of a part')),
        # ('Tehnic', _('Technician')),
        # ('ZKBPDP', _('Deputy Battalion Commander for Airborne Training')),
        # ('ZKBNSH', _('Chief of Staff - First Deputy Battalion Commander')), 
        # ('SPZKISCH', _('Senior assistant chief of staff for personnel and military units')),
    )
    name = models.CharField(max_length=512, verbose_name=_('Name'), choices=CHOICES)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    def __str__(self):
        return self.get_name_display()

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')


class Order(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'), blank=True)
    osoba = models.ManyToManyField(ServiseID, verbose_name= _('osoba'))
    order_number = models.CharField(max_length=512, verbose_name=_('order number'))
    order_date = models.DateField(verbose_name=_('order date'), default=timezone.now )
    appruve = models.BooleanField(verbose_name=_('order number'), default=False)
    appruve_date = models.DateField(verbose_name=_('appruve date'), default=timezone.now )
    status = models.ForeignKey(StatusOrder, on_delete=models.CASCADE, verbose_name= _('status'), null=True)
    
    def __str__(self):
        return '{} №{}'.format(self.name[:50], self.order_number)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Order\'s')



