# Generated by Django 4.2.13 on 2024-06-16 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_alter_place_lat_alter_place_lng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeimage',
            name='image',
            field=models.ImageField(db_index=True, upload_to='', verbose_name='Фото'),
        ),
    ]
