# Generated by Django 3.2.6 on 2021-09-15 08:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210915_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='appruve_date',
            field=models.DateField(default=datetime.datetime(2021, 9, 15, 8, 27, 34, 351276, tzinfo=utc), verbose_name='Дата прийому на службу'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2021, 9, 15, 8, 27, 34, 351276, tzinfo=utc), verbose_name='Дата наказу'),
        ),
    ]