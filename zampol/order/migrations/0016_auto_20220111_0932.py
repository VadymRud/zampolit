# Generated by Django 3.2.10 on 2022-01-11 07:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_alter_allcontract_osoba'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allcontract',
            options={'verbose_name': 'Контракт', 'verbose_name_plural': 'Контракти'},
        ),
        migrations.AlterField(
            model_name='allcontract',
            name='date_begin',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Начало контракта'),
        ),
        migrations.AlterField(
            model_name='allcontract',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Наказ'),
        ),
    ]
