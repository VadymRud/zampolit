# Generated by Django 3.1.6 on 2021-02-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osoba', '0008_auto_20210223_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviseid',
            name='military_rank_date',
            field=models.DateField(blank=True, null=True, verbose_name='Військовий квиток дата видачі'),
        ),
        migrations.AddField(
            model_name='serviseid',
            name='military_rank_id',
            field=models.CharField(blank=True, max_length=1020, null=True, verbose_name='military_rank_id'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='ID_date',
            field=models.DateField(blank=True, null=True, verbose_name='Паспорт дата видачі'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='ID_number',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Паспорт номер'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='ID_seria',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='Паспорт серія'),
        ),
        migrations.AlterField(
            model_name='serviseid',
            name='who_ID',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Хто видав Паспорт'),
        ),
    ]