from django.db import models

class MilitaryRanks(models.Model):
    name = models.CharField(max_length=512)


class ServiseID(models.Model):
    name = models.CharField(max_length=512)
    sename = models.CharField(max_length=512)
    thirdName = models.CharField(max_length=512)
    birthDate = models.DateField()




