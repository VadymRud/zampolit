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

def image_directory_path(instance, filename): 
    return 'images/{}/{}/{}_{}_{}/{}'.format(instance.unit, instance.platoon, instance.name, \
         instance.sename, instance.third_name, filename) 


class ServiseID(models.Model):
    name = models.CharField(max_length=512)
    sename = models.CharField(max_length=512)
    third_name = models.CharField(max_length=512)
    birth_date = models.DateField()
    military_ranks = models.ForeignKey(MilitaryRank, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    platoon = models.ForeignKey(Platoon, on_delete=models.CASCADE)
    image3x4 = models.BinaryField(blank=True)
    image_face3x4 = models.ImageField(upload_to=image_directory_path, blank=True)
    
    def __str__(self):
        return '{} {} {} {} {}'.format(self.unit.name, self.military_ranks.name, self.name ,self.sename, self.third_name)
