# Generated by Django 3.1.6 on 2021-06-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osoba', '0005_auto_20210430_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviseid',
            name='addres_fact',
            field=models.TextField(blank=True, null=True, verbose_name='addres_fact'),
        ),
        migrations.AddField(
            model_name='serviseid',
            name='addres_pr',
            field=models.TextField(blank=True, null=True, verbose_name='addres_pr'),
        ),
    ]