# Generated by Django 3.1.6 on 2021-02-14 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osoba', '0003_serviseid_image3x4'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviseid',
            name='image_face3x4',
            field=models.ImageField(blank=True, upload_to='<django.db.models.fields.related.ForeignKey>/<django.db.models.fields.related.ForeignKey>/<django.db.models.fields.CharField>_<django.db.models.fields.CharField>_<django.db.models.fields.CharField>/'),
        ),
    ]
