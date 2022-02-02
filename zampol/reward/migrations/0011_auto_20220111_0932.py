# Generated by Django 3.2.10 on 2022-01-11 07:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_auto_20220111_0932'),
        ('reward', '0010_interview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interview',
            options={'verbose_name': 'Співбесіда', 'verbose_name_plural': 'Співбесіда'},
        ),
        migrations.AlterModelOptions(
            name='rewardocoba',
            options={'verbose_name': 'Особа, яка дала догану чи нагороду', 'verbose_name_plural': 'Особи, які дали догану чи нагороду'},
        ),
        migrations.AlterModelOptions(
            name='typepenalty',
            options={'verbose_name': 'Догана', 'verbose_name_plural': 'Типи Доган'},
        ),
        migrations.AlterModelOptions(
            name='typereward',
            options={'verbose_name': 'Нагорода', 'verbose_name_plural': 'Нагороди'},
        ),
        migrations.AlterField(
            model_name='interview',
            name='interview_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата прийому на службу'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='opinion',
            field=models.CharField(blank=True, max_length=512, verbose_name='Висновок'),
        ),
        migrations.AlterField(
            model_name='interview',
            name='topic',
            field=models.CharField(blank=True, max_length=512, verbose_name='Тема співбесіди'),
        ),
        migrations.AlterField(
            model_name='penalty',
            name='date_cancel',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата закінчення'),
        ),
        migrations.AlterField(
            model_name='penalty',
            name='order',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Наказ'),
        ),
        migrations.AlterField(
            model_name='penalty',
            name='osoba_cancel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='reward.rewardocoba', verbose_name='Особа, яка закрила'),
        ),
        migrations.AlterField(
            model_name='penalty',
            name='penalty_ocoba',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='reward.rewardocoba', verbose_name='Хто дав догану'),
        ),
        migrations.AlterField(
            model_name='penalty',
            name='type_penalty',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='reward.typepenalty', verbose_name='Типи доган'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='order',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='Наказ'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='reward_ocoba',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='reward.rewardocoba', verbose_name='Заоохочення та нагороди'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='type_reward',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='reward.typereward', verbose_name='Заоохочення та нагороди'),
        ),
    ]
