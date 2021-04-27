# Generated by Django 3.1.6 on 2021-04-27 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('osoba', '0010_auto_20210427_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='SHPK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name="Ім'я")),
            ],
            options={
                'verbose_name': 'ШПК',
                'verbose_name_plural': 'ШПК',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, verbose_name="Ім'я")),
                ('vos', models.CharField(max_length=512, verbose_name='ВОС')),
                ('salary', models.PositiveBigIntegerField(verbose_name='Оклад')),
                ('tariff_category', models.PositiveBigIntegerField(verbose_name='Тарифний розряд')),
                ('company', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='osoba.company', verbose_name='Підрозділ')),
                ('ocoba', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='osoba.serviseid', verbose_name='ocoba')),
                ('shpk', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='staff.shpk', verbose_name='ШПК')),
            ],
            options={
                'verbose_name': 'Штатка',
                'verbose_name_plural': 'Штатка',
            },
        ),
    ]
