# Generated by Django 4.1 on 2022-09-08 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_friendmail_truckfriendmail_traileroffer_trailermail_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trailerfriendmail',
            old_name='truck',
            new_name='trailer',
        ),
    ]
