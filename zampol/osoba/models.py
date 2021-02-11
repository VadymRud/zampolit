from django.db import models


class MilitaryRank(models.Model):
    name = models.CharField(max_length=512)
    
    def __str__(self):
        return self.name[:50]


class Platoon(models.Model):
    name = models.CharField(max_length=512)
    
    def __str__(self):
        return self.name[:50]


class Unit(models.Model):
    name = models.CharField(max_length=512)
    
    def __str__(self):
        return self.name[:50]


class ServiseID(models.Model):
    name = models.CharField(max_length=512)
    sename = models.CharField(max_length=512)
    third_name = models.CharField(max_length=512)
    birth_date = models.DateField()
    military_ranks = models.ForeignKey(MilitaryRank, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    platoon = models.ForeignKey(Platoon, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} {} {} {} {}'.format(self.unit.name, self.military_ranks.name, self.name ,self.sename, self.third_name)
