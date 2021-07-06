# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adresa(models.Model):
    adr_id = models.AutoField(unique=True)
    adr_n_id = models.IntegerField()
    adresa = models.CharField()

    class Meta:
        managed = False
        db_table = 'adresa'


class Kontrakt(models.Model):
    kontrakt_com_id = models.AutoField(unique=True)
    kontrakt_com_n_id = models.IntegerField()
    kontrakt_date = models.DateField()
    kontrakt_srok = models.IntegerField()
    kontrakt_zak = models.DateField()

    class Meta:
        managed = False
        db_table = 'kontrakt'


class Nakaz(models.Model):
    nak_id = models.AutoField(unique=True)
    nak_n_id = models.IntegerField()
    nak_status_id = models.IntegerField()
    zvidky = models.IntegerField()
    kudy = models.IntegerField()
    nak_data = models.DateField()
    nak_nomer = models.IntegerField()
    povern = models.DateField()
    tmp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nakaz'


class NakazNomer(models.Model):
    n_nak_id = models.AutoField()
    n_nak_data = models.DateField()
    n_nak_nomer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nakaz_nomer'


class NakazPlace(models.Model):
    nak_place_id = models.AutoField(unique=True)
    nak_place_name = models.CharField()

    class Meta:
        managed = False
        db_table = 'nakaz_place'


class Name(models.Model):
    n_id = models.AutoField(unique=True)
    name = models.TextField()
    short_name = models.TextField()
    pseudo = models.CharField()
    zv_id = models.IntegerField()
    data_zv = models.CharField()
    pos_id = models.IntegerField()
    pos_id_old = models.IntegerField()
    p_id = models.IntegerField()
    kontr = models.TextField()  # This field type is a guess.
    data_narod = models.DateField()
    adresa_nar = models.CharField()
    data_mob = models.DateField()
    vijskomat = models.CharField()
    data_zarah = models.DateField()
    nomer_nakazu_ok = models.CharField()
    data_nakazu_ok = models.DateField()
    chiy_nakaz = models.CharField()
    kontrakt = models.DateField()
    kontrakt_strok = models.CharField()
    kontrakt_zak = models.DateField()
    nomer_nakazu = models.IntegerField()
    data_zviln = models.DateField()
    nomer_nakazu_zviln = models.IntegerField()
    nomer_pasp = models.CharField()
    code_nomer = models.CharField()
    voen_nomer = models.CharField()
    grupa_krovi = models.CharField()
    osvita = models.IntegerField()
    specialnist = models.CharField()
    zvp = models.CharField()
    fahova = models.CharField()
    liderstvo = models.CharField()
    perem = models.CharField()
    persh_kontr = models.CharField()
    ozdor = models.CharField()
    mdspp = models.CharField()
    sim_stan = models.TextField()  # This field type is a guess.
    stats = models.TextField()  # This field type is a guess.
    status = models.IntegerField()
    status2 = models.IntegerField()
    notes = models.TextField()
    notes1 = models.TextField()

    class Meta:
        managed = False
        db_table = 'name'


class OsvitaName(models.Model):
    osv_name_id = models.AutoField(unique=True)
    osv_name = models.CharField()

    class Meta:
        managed = False
        db_table = 'osvita_name'


class Peremish(models.Model):
    perem_id = models.AutoField(unique=True)
    perem_n_id = models.IntegerField()
    perem_status_id = models.IntegerField()
    zvidky = models.IntegerField()
    kudy = models.IntegerField()
    perem_data = models.DateField()
    nakaz_id = models.IntegerField()
    povern = models.DateField()

    class Meta:
        managed = False
        db_table = 'peremish'


class Phones(models.Model):
    ph_id = models.AutoField(unique=True)
    n_id = models.IntegerField()
    ph_nomer = models.TextField()

    class Meta:
        managed = False
        db_table = 'phones'


class PidrozdilId(models.Model):
    p_id = models.AutoField(unique=True)
    p_parent_id = models.IntegerField()
    isparent = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pidrozdil_id'


class PidrozdilName(models.Model):
    p_id = models.AutoField(unique=True)
    por_nomer = models.IntegerField()
    p_name = models.TextField()
    p_short_name = models.CharField()
    p_full_name = models.CharField()
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pidrozdil_name'


class PosadaName(models.Model):
    pos_id = models.AutoField(unique=True)
    pos_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'posada_name'


class Priznach(models.Model):
    prizn_id = models.AutoField()
    prizn_n_id = models.IntegerField()
    prizn_data = models.DateField()
    prizn_pos_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'priznach'


class PriznachOld(models.Model):
    prizn_id = models.AutoField()
    prizn_n_id = models.IntegerField()
    prizn_data = models.DateField()
    prizn_pos_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'priznach_old'


class PriznachOld2(models.Model):
    prizn_id = models.AutoField()
    prizn_n_id = models.IntegerField()
    prizn_data = models.DateField()
    prizn_pos_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'priznach_old_2'


class Ridny(models.Model):
    rid_id = models.AutoField(unique=True)
    rid_n_id = models.IntegerField()
    rid_name_id = models.IntegerField()
    rid_name = models.CharField()
    rid_data_nar = models.DateField()
    rid_phone = models.IntegerField()
    rid_notes = models.CharField()

    class Meta:
        managed = False
        db_table = 'ridny'


class RidnyName(models.Model):
    rid_name_id = models.AutoField(unique=True)
    rid_name_name = models.CharField()

    class Meta:
        managed = False
        db_table = 'ridny_name'


class Shtatka(models.Model):
    pos_id = models.AutoField(unique=True)
    p_id = models.IntegerField()
    sh_id = models.IntegerField()
    zv_sh_id = models.IntegerField()
    dopusk = models.CharField()
    vos = models.CharField()
    oklad = models.CharField()
    vidsotok = models.IntegerField()
    nomer_kniga = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shtatka'


class ShtatkaOld(models.Model):
    pos_id = models.AutoField(unique=True)
    p_id = models.IntegerField()
    sh_id = models.IntegerField()
    zv_sh_id = models.IntegerField()
    vos = models.CharField()
    oklad = models.CharField()
    nomer_kniga = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shtatka_old'


class ShtatkaOld2(models.Model):
    pos_id = models.AutoField(unique=True)
    p_id = models.IntegerField()
    sh_id = models.IntegerField()
    zv_sh_id = models.IntegerField()
    vos = models.CharField()
    oklad = models.CharField()
    nomer_kniga = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shtatka_old_2'


class SimStanName(models.Model):
    s_stan_name_id = models.AutoField(unique=True)
    s_stan_name = models.CharField()

    class Meta:
        managed = False
        db_table = 'sim_stan_name'


class StatsName(models.Model):
    s_stats_name_id = models.AutoField()
    s_stats_name = models.CharField()

    class Meta:
        managed = False
        db_table = 'stats_name'


class StatusName(models.Model):
    s_id = models.AutoField(unique=True)
    s_name = models.CharField()

    class Meta:
        managed = False
        db_table = 'status_name'


class Table32(models.Model):
    col_1 = models.CharField(db_column='COL 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_2 = models.IntegerField(db_column='COL 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'table 32'


class Table35(models.Model):
    col_1 = models.CharField(db_column='COL 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    col_2 = models.IntegerField(db_column='COL 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'table 35'


class Temp(models.Model):
    number_1 = models.IntegerField(db_column='1')  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.TextField(db_column='2')  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'temp'


class Tmp(models.Model):
    number_1 = models.IntegerField(db_column='1')  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.TextField(db_column='2')  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'tmp'


class Vysluga(models.Model):
    vys_id = models.AutoField()
    vys_n_id = models.IntegerField()
    vys_data_mob = models.DateField()
    vys_data_zvil = models.DateField()

    class Meta:
        managed = False
        db_table = 'vysluga'


class VyslugaNormy(models.Model):
    rokiv = models.IntegerField()
    nadbavka = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vysluga_normy'


class VyslugaZv(models.Model):
    vys_zv_id = models.AutoField()
    vys_zv_n_id = models.IntegerField()
    data_zv = models.DateField()

    class Meta:
        managed = False
        db_table = 'vysluga_zv'


class ZbrStatusName(models.Model):
    zbr_status_id = models.AutoField(unique=True)
    zbr_status_name = models.CharField()

    class Meta:
        managed = False
        db_table = 'zbr_status_name'


class Zbroya(models.Model):
    zbr_id = models.AutoField(unique=True)
    zbr_type = models.IntegerField()
    nomer = models.CharField()
    n_id = models.IntegerField()
    magazin = models.IntegerField()
    zbr_status = models.IntegerField()
    zbr_note = models.CharField()

    class Meta:
        managed = False
        db_table = 'zbroya'


class ZbroyaAll(models.Model):
    zbr_type = models.IntegerField()
    nomer = models.CharField()
    rota = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zbroya_all'


class ZbroyaName(models.Model):
    zbr_id = models.AutoField(unique=True)
    zbr_name = models.CharField()

    class Meta:
        managed = False
        db_table = 'zbroya_name'


class ZbroyaSklad(models.Model):
    zbr_type = models.IntegerField()
    nomer = models.CharField()

    class Meta:
        managed = False
        db_table = 'zbroya_sklad'


class ZvGrupaName(models.Model):
    zv_gr_id = models.AutoField(unique=True)
    zv_gr_name = models.CharField()

    class Meta:
        managed = False
        db_table = 'zv_grupa_name'


class ZvannyaId(models.Model):
    zv_id = models.IntegerField(unique=True)
    zv_gr_id = models.IntegerField()
    zv_okl = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zvannya_id'


class ZvannyaName(models.Model):
    zv_id = models.AutoField(unique=True)
    zv_name = models.TextField()
    zv_short_name = models.CharField()

    class Meta:
        managed = False
        db_table = 'zvannya_name'


class ZvilnComent(models.Model):
    zv_com_id = models.AutoField(unique=True)
    zv_com_n_id = models.IntegerField()
    zv_coment = models.CharField()

    class Meta:
        managed = False
        db_table = 'zviln_coment'
