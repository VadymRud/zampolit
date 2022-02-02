# Generated by Django 3.2.10 on 2022-01-11 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('osoba', '0021_auto_20220106_1244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Райони', 'verbose_name_plural': 'Райони'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name': 'Область', 'verbose_name_plural': 'Області'},
        ),
        migrations.AddField(
            model_name='serviseid',
            name='driveid_category',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='driveid category'),
        ),
        migrations.AlterField(
            model_name='command',
            name='name',
            field=models.CharField(choices=[('KB', 'Командир батальйону'), ('ZKB', 'Замісник командира батальйону'), ('ZKBMPZ', 'Замісник командира батальйону з морально-психологічної роботи'), ('PKBZPR', 'Помічник командира батальйону з юридичних питань'), ('OP', 'Офіцер-психолог'), ('GSVCH', 'Головний сержант батальйону'), ('Tehnic', 'Технік'), ('ZKBPDP', 'Заступник командира батальйону з повітряно-десантної підготовки'), ('ZKBNSH', 'Начальник штабу - перший заступник командира батальйону'), ('SPZKISCH', 'Старший помічник начальника штабу з кадрів і стройової частини')], max_length=512, verbose_name='Командування'),
        ),
        migrations.AlterField(
            model_name='command',
            name='temporarily',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='ТВО'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='addres_fact',
            field=models.TextField(blank=True, null=True, verbose_name='адреса фактичного проживання'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='father',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Батько'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='military_office',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Воєнкомат'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='mother',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Мати'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='name_accs',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name="Ім'я В/С в давальному відмінку"),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='partner',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Чоловік або дружина'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='phone1',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Домашній телефон'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='phone2',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Мобільний телефон'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='postal_code_fact',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Поштовий індекс'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='postal_code_pr',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Індекс прописки'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='region_fact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='osoba.region', verbose_name='Район проживання'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='region_pr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='osoba.region', verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='sename_accs',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Прізвище в давальному відмінку'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='state_fact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='osoba.state', verbose_name='Область проживання'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='state_pr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='osoba.state', verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='third_name_accs',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='По батькові в давальному відмінку'),
        ),
    ]