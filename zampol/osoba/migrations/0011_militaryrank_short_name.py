# Generated by Django 3.2.6 on 2021-08-16 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osoba', '0010_auto_20210813_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='militaryrank',
            name='short_name',
            field=models.CharField(default=2, max_length=512, verbose_name='Short name'),
            preserve_default=False,
        ),
    ]
