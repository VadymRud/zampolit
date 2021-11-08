# Generated by Django 3.2.6 on 2021-10-28 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0005_shpk_short_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=512, verbose_name="Ім'я")),
                ('text', models.TextField(verbose_name='text')),
                ('staff', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staff', verbose_name='staff')),
            ],
            options={
                'verbose_name': 'Reward',
                'verbose_name_plural': 'Rewards',
            },
        ),
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=512, verbose_name="Ім'я")),
                ('text', models.TextField(verbose_name='text')),
                ('staff', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staff', verbose_name='staff')),
            ],
            options={
                'verbose_name': 'Penalty',
                'verbose_name_plural': 'Penalties',
            },
        ),
    ]
