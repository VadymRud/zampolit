from django.db import models
from django.utils.translation import gettext as _
from django.conf.global_settings import STATIC_ROOT

class MilitaryRank(models.Model):
    name = models.CharField(max_length=512, verbose_name= _('Name'))
    
    def __str__(self):
        return self.name[:50]
    
    class Meta:
        verbose_name = _('Military Rank')
        verbose_name_plural = _('Military Ranks')



class Platoon(models.Model):
    name = models.CharField(max_length=512, verbose_name= _('Name'))
    
    def __str__(self):
        return self.name[:50]

    class Meta:
        verbose_name = _('Platoon')
        verbose_name_plural = _('Platoons')



class Unit(models.Model):
    name = models.CharField(max_length=512, verbose_name= _('Name'))
    
    def __str__(self):
        return self.name[:50]
    
    class Meta:
        verbose_name = _('Unit')
        verbose_name_plural = _('Units')
    

class Company(models.Model):
    name = models.CharField(max_length=512, verbose_name= _('Name'))
    
    def __str__(self):
        return self.name[:50]
    
    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Company')



class OfficialPosition(models.Model):
    name = models.CharField(max_length=512, verbose_name= _('Name'))
    shpk = models.CharField(max_length=512, verbose_name= _('SHPK'))

    def __str__(self):
        return self.name[:50]
    
    class Meta:
        verbose_name = _('Official Position')
        verbose_name_plural = _('Official Positions')


def image_directory_path(instance, filename): 
    return '{}/images/{}/{}/{}_{}_{}/{}'.format('media',instance.unit, instance.platoon, instance.name, \
         instance.sename, instance.third_name, filename) 


class ServiseID(models.Model):
    name = models.CharField(max_length=512, verbose_name= _('Name Person'))
    sename = models.CharField(max_length=512, verbose_name= _('Sename'))
    third_name = models.CharField(max_length=512, verbose_name= _('third name'))
    birth_date = models.DateField(verbose_name= _('birth date'))
    military_ranks = models.ForeignKey(MilitaryRank, on_delete=models.CASCADE, verbose_name= _('military rank'))
    # company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name= _('company'))
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, verbose_name= _('unit'))
    platoon = models.ForeignKey(Platoon, on_delete=models.CASCADE, blank=True, verbose_name= _('platoon'))
    image3x4 = models.BinaryField(blank=True, verbose_name= _('image3x4'))
    image_face3x4 = models.ImageField(upload_to=image_directory_path, blank=True, verbose_name= _('image_face3x4'))
    official_position = models.ForeignKey(OfficialPosition, on_delete=models.CASCADE, blank=True, verbose_name= _('official_position'))
    # інфо про призов 
    def __str__(self):
        return '{} {} {} {} {}'.format(self.unit.name, self.military_ranks.name, self.name ,self.sename, self.third_name)

    class Meta:
        verbose_name = _('ServiseID')
        verbose_name_plural = _('ServiseIDs')
