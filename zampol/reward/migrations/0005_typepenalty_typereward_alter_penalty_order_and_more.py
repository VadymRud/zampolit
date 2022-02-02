# Generated by Django 4.0 on 2021-12-29 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_statusorder_name'),
        ('reward', '0004_penalty_order_reward_order_alter_penalty_osoba_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypePenalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=512, verbose_name="Ім'я")),
            ],
        ),
        migrations.CreateModel(
            name='TypeReward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=512, verbose_name="Ім'я")),
            ],
        ),
        migrations.AlterField(
            model_name='penalty',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='order'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reward',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='penalty',
            name='type_penalty',
            field=models.ForeignKey(blank=True, null=True,  on_delete=django.db.models.deletion.CASCADE, to='reward.typepenalty', verbose_name='Type Penalty'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reward',
            name='type_reward',
            field=models.ForeignKey(blank=True, null=True,  on_delete=django.db.models.deletion.CASCADE, to='reward.typereward', verbose_name='Type Reward'),
            preserve_default=False,
        ),
    ]
