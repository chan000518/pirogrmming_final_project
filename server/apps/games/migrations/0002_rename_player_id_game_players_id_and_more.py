# Generated by Django 5.0.1 on 2024-02-14 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='player_id',
            new_name='players_id',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='player_name',
            new_name='players_name',
        ),
    ]
