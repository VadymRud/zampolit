from django.db import models
from django.utils import timezone
from staff.models import Staff
from django.utils.translation import gettext as _


class Reward(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'), blank=True)
    reward_date = models.DateField(verbose_name=_('order date'), default=timezone.now )
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, verbose_name= _('staff'))
    text = models.TextField(verbose_name= _('text'), blank=True, null=True)
    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Reward')
        verbose_name_plural = _('Rewards')


class Penalty(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'), blank=True)
    penalty_date = models.DateField(verbose_name=_('order date'), default=timezone.now )
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, verbose_name= _('staff'))
    text = models.TextField(verbose_name= _('text'), blank=True, null=True)
    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Penalty')
        verbose_name_plural = _('Penalties')
