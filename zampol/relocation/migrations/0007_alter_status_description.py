# Generated by Django 4.0 on 2021-12-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relocation', '0006_auto_20210915_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='description',
            field=models.TextField(blank=True, verbose_name='Дата призову'),
        ),
    ]