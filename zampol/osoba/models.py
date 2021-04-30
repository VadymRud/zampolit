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


class Creed(models.Model):
    name = models.CharField(max_length=512, verbose_name= _('Name'))
    
    def __str__(self):
        return self.name[:50]
    
    class Meta:
        verbose_name = _('Creed')
        verbose_name_plural = _('Creed')


class Nationality(models.Model):
    name = models.CharField(max_length=512, verbose_name= _('Name'))
    
    def __str__(self):
        return self.name[:50]
    
    class Meta:
        verbose_name = _('Nationality')
        verbose_name_plural = _('Nationalities')


class Education(models.Model):
    name = models.CharField(max_length=512, verbose_name= _('Name'))
    
    def __str__(self):
        return self.name[:50]
    
    class Meta:
        verbose_name = _('Education')
        verbose_name_plural = _('Education')


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
    platoon = models.ForeignKey(Platoon, on_delete=models.CASCADE, blank=True, verbose_name= _('platoon'), null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, verbose_name= _('unit'), null=True)
    image3x4 = models.BinaryField(blank=True, verbose_name= _('image3x4'))
    image_face3x4 = models.ImageField(upload_to=image_directory_path, blank=True, verbose_name= _('image_face3x4'))
    official_position = models.ForeignKey(OfficialPosition, on_delete=models.CASCADE, blank=True, verbose_name= _('official_position'))
    # інфо про призов
    military_office = models.CharField(max_length=1024, verbose_name= _('Military office'), blank=True, null=True)
    date_of_conscription = models.DateField(verbose_name= _('date of conscription'), blank=True, null=True)
    order_date = models.DateField(verbose_name= _('order date'), blank=True, null=True)
    order_number = models.CharField(max_length=100, verbose_name= _('order number'), blank=True, null=True)
    # військовий квиток
    militaryID_seria = models.CharField(max_length=3, verbose_name= _('militaryID seria'), blank=True, null=True)
    militaryID_number = models.CharField(max_length=10, verbose_name= _('militaryID number'), blank=True, null=True)
    who_militaryID = models.CharField(max_length=10, verbose_name= _('who_militaryID'), blank=True, null=True)
    militaryID_date = models.DateField(verbose_name= _('militaryID_date'), blank=True, null=True)
    weapon =  models.CharField(max_length=1020, verbose_name= _('weapon'), blank=True, null=True)
    military_rank_id = models.CharField(max_length=1020, verbose_name= _('military_rank_id'), blank=True, null=True)
    military_rank_date = models.DateField(verbose_name= _('military_rank_date'), blank=True, null=True)

    # паспорт
    ID_seria = models.CharField(max_length=3, verbose_name= _('ID seria'), blank=True, null=True)
    ID_number = models.CharField(max_length=10, verbose_name= _('ID number'), blank=True, null=True)
    who_ID = models.CharField(max_length=10, verbose_name= _('who_ID'), blank=True, null=True)
    ID_date = models.DateField(verbose_name= _('ID_date'), blank=True, null=True)
    ipn = models.CharField(max_length=10, verbose_name= _('ipn'), blank=True, null=True)

    # загальна інформація
    orphan = models.BooleanField(_('orphan'), default=False, help_text=_('orphan'))
    married  = models.BooleanField(_('married'), default=False)
    halforphan  = models.BooleanField(_('halforphan'), default=False)
    work = models.BooleanField(_('work'), default=False)
    mobilization  = models.BooleanField(_('mobilization'), default=False)
    driveid  = models.BooleanField(_('driveid'), default=False)
    creed = models.ForeignKey(Creed, on_delete=models.CASCADE, blank=True, null =True, verbose_name= _('creed'))
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, blank=True, null =True, verbose_name= _('nationality'))
    education = models.ForeignKey(Education, on_delete=models.CASCADE, blank=True, null =True, verbose_name= _('Education'))
    blood_type = models.CharField(max_length=3, verbose_name= _('blood_type'), blank=True, null=True)
    rh = models.CharField(max_length=2, verbose_name= _('RH'), blank=True, null=True)


    def __str__(self):
        return '{} {} {} {} {}'.format(self.unit.name, self.military_ranks.name, self.name ,self.sename, self.third_name)

    class Meta:
        verbose_name = _('ServiseID')
        verbose_name_plural = _('ServiseIDs')
