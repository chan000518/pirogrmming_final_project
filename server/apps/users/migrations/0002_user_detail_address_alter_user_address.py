# Generated by Django 5.0.1 on 2024-02-06 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='detail_address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
