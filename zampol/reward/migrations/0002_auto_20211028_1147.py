# Generated by Django 3.2.6 on 2021-10-28 08:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reward', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='penalty',
            name='penalty_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата наказу'),
        ),
        migrations.AddField(
            model_name='reward',
            name='reward_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата наказу'),
        ),
        migrations.AlterField(
            model_name='penalty',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='text'),
        ),
    ]
