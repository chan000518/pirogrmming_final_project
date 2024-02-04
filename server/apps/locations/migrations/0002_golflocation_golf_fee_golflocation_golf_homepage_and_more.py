# Generated by Django 5.0.1 on 2024-02-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='golflocation',
            name='golf_fee',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='golflocation',
            name='golf_homepage',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='golflocation',
            name='golf_reservation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='golflocation',
            name='golf_reservepage',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='golflocation',
            name='golf_runningdate',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='golflocation',
            name='golf_runningtime',
            field=models.TextField(blank=True, null=True),
        ),
    ]
