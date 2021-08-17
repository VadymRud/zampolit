# Generated by Django 3.2.6 on 2021-08-16 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_rename_unic_staff_unicum'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='id',
            field=models.BigAutoField(auto_created=True, default=5, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staff',
            name='unicum',
            field=models.PositiveBigIntegerField(unique=True, verbose_name='Unic number'),
        ),
    ]