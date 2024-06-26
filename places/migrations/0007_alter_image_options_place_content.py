# Generated by Django 4.2.13 on 2024-06-02 13:29

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_image_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='place',
            name='content',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
