# Generated by Django 4.1 on 2022-09-02 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0005_truckexterior_roof_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='truckengine',
            name='engine_manufacturer',
        ),
        migrations.RemoveField(
            model_name='truckpowertrain',
            name='transmission_manufacturer',
        ),
        migrations.DeleteModel(
            name='EngineManufacturer',
        ),
        migrations.DeleteModel(
            name='TransmissionManufacturer',
        ),
    ]