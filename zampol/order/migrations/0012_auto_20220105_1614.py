# Generated by Django 3.2.10 on 2022-01-05 14:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('osoba', '0017_auto_20210915_1639'),
        ('order', '0011_auto_20220105_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allcontract',
            name='date_begin',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='contract begin'),
        ),
        migrations.RemoveField(
            model_name='allcontract',
            name='osoba',
        ),
        migrations.AddField(
            model_name='allcontract',
            name='osoba',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='osoba.serviseid', verbose_name='Військовослужбовець'),
            preserve_default=False,
        ),
    ]
