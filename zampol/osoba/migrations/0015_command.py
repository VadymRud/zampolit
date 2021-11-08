# Generated by Django 3.2.6 on 2021-09-15 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('osoba', '0014_remove_serviseid_official_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('KB', 'Battalion commander'), ('ZKB', 'Deputy Battalion Commander'), ('ZKBMPZ', 'Deputy Battalion Commander for Moral and Psychological Support'), ('PKBZPR', 'Assistant Battalion Commander for Legal Affairs'), ('OP', 'Officer-psychologist'), ('GSVCH', 'Chief sergeant of a military unit'), ('Tehnic', 'Technician'), ('ZKBPDP', 'Deputy Battalion Commander for Airborne Training'), ('ZKBNSH', 'Chief of Staff - First Deputy Battalion Commander'), ('SPZKISCH', 'Senior assistant chief of staff for personnel and military units')], max_length=512, verbose_name='Name Command')),
                ('temporarily', models.PositiveSmallIntegerField(default=0, max_length=1, verbose_name='TVO')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osoba.serviseid', verbose_name="Ім'я В/С")),
            ],
        ),
    ]
