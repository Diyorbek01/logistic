# Generated by Django 4.1 on 2022-09-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0023_alter_truckchassis_gvw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truckchassis',
            name='gvw',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
