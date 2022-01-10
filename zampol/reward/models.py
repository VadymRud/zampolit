from django.db import models
from django.utils import timezone
from staff.models import Staff
from osoba.models import ServiseID
from order.models import Order
from django.utils.translation import gettext as _


class TypeReward(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'), blank=True)

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Type of reward')
        verbose_name_plural = _('Types of rewards')


class TypePenalty(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'), blank=True)

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Type of penalty')
        verbose_name_plural = _('Types of penalties')


class RewardOcoba(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'), blank=True)

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Reward or Penalty ocoba')
        verbose_name_plural = _('Rewards or Penalty ocobs')


class Reward(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'), blank=True)
    reward_date = models.DateField(verbose_name=_('order date'), default=timezone.now)
    osoba = models.ForeignKey(ServiseID, on_delete=models.CASCADE, blank=True, verbose_name=_('osoba'))
    text = models.TextField(verbose_name=_('text'), blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, verbose_name=_('order'))
    type_reward = models.ForeignKey(TypeReward, on_delete=models.CASCADE, blank=True, verbose_name=_('Type Reward'))
    reward_ocoba = models.ForeignKey(RewardOcoba, on_delete=models.CASCADE, blank=True, verbose_name=_('Reward Ocoba'))

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Reward')
        verbose_name_plural = _('Rewards')


class Penalty(models.Model):
    name = models.CharField(max_length=512, verbose_name=_('Name'), blank=True)
    penalty_date = models.DateField(verbose_name=_('order date'), default=timezone.now)
    osoba = models.ForeignKey(ServiseID, on_delete=models.CASCADE, blank=True, verbose_name=_('osoba'))
    text = models.TextField(verbose_name=_('text'), blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, verbose_name=_('order'))
    type_penalty = models.ForeignKey(TypePenalty, on_delete=models.CASCADE, blank=True, verbose_name=_('Type Penalty'))
    penalty_ocoba = models.ForeignKey(RewardOcoba, on_delete=models.CASCADE, blank=True, verbose_name=_('Penalty Ocoba'),
                                      related_name='+')
    date_cancel = models.DateField(verbose_name=_('date Cansel'), default=timezone.now, blank=True, null=True)
    osoba_cancel = models.ForeignKey(RewardOcoba, on_delete=models.CASCADE, blank=True, null=True,
                                     verbose_name=_('Ocoba Cansel'), related_name='+')

    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Penalty')
        verbose_name_plural = _('Penalties')


class Interview(models.Model):

    interview_date = models.DateField(verbose_name=_('Interview date'), default=timezone.now)
    osoba = models.ForeignKey(ServiseID, on_delete=models.CASCADE, blank=True, verbose_name=_('osoba'))
    topic = models.CharField(max_length=512, verbose_name=_('Interview topic'), blank=True)
    opinion = models.CharField(max_length=512, verbose_name=_('Interview opinion'), blank=True)

    def __str__(self):
        return '{} {} {}'.format(self.interview_date, self.osoba, self.topic[:50])

    class Meta:
        verbose_name = _('Interview')
        verbose_name_plural = _('Interview')
