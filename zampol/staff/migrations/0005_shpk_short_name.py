# Generated by Django 3.2.6 on 2021-08-16 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_auto_20210816_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='shpk',
            name='short_name',
            field=models.CharField(default=4, max_length=512, verbose_name='Short name'),
            preserve_default=False,
        ),
    ]