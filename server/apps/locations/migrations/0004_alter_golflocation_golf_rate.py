# Generated by Django 5.0.1 on 2024-02-13 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_alter_golflocation_golf_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golflocation',
            name='golf_rate',
            field=models.FloatField(default=5.0),
        ),
    ]
