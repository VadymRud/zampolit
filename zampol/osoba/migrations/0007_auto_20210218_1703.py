# Generated by Django 3.1.6 on 2021-02-18 14:03

from django.db import migrations, models
import django.db.models.deletion
import osoba.models


class Migration(migrations.Migration):

    dependencies = [
        ('osoba', '0006_auto_20210218_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=512, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='militaryrank',
            name='name',
            field=models.CharField(max_length=512, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='officialposition',
            name='name',
            field=models.CharField(max_length=512, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='officialposition',
            name='shpk',
            field=models.CharField(max_length=512, verbose_name='ШПК'),
        ),
        migrations.AlterField(
            model_name='platoon',
            name='name',
            field=models.CharField(max_length=512, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='birth_date',
            field=models.DateField(verbose_name='Дата народження'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='image_face3x4',
            field=models.ImageField(blank=True, upload_to=osoba.models.image_directory_path, verbose_name='Фотокартка 3 на 4'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='military_ranks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osoba.militaryrank', verbose_name='Військове звання'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='official_position',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='osoba.officialposition', verbose_name='Посада'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='platoon',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='osoba.platoon', verbose_name='Взвод'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='unit',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='osoba.unit', verbose_name='Рота'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=512, verbose_name="Ім'я"),
        ),
    ]
