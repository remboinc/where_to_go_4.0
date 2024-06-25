# Generated by Django 4.2.13 on 2024-06-25 20:50

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0015_alter_placeimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, default='Без описания... пока', verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, default='Без описания... пока', verbose_name='Краткое описание'),
        ),
    ]
