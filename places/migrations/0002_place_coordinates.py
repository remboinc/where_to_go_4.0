# Generated by Django 4.2.13 on 2024-05-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='coordinates',
            field=models.JSONField(default=dict),
        ),
    ]
