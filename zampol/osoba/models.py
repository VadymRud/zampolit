from django.db import models


class MilitaryRanks(models.Model):
    name = models.CharField(max_length=512)


class Platoon(models.Model):
    name = models.CharField(max_length=512)


class Unit(models.Model):
    name = models.CharField(max_length=512)


class ServiseID(models.Model):
    name = models.CharField(max_length=512)
    sename = models.CharField(max_length=512)
    third_name = models.CharField(max_length=512)
    birth_date = models.DateField()
    military_ranks = models.ForeignKey(MilitaryRanks, on_delete=models.SET_NULL)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL)
    platoon = models.ForeignKey(Platoon, on_delete=models.SET_NULL)
