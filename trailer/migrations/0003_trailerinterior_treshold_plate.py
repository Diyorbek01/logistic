# Generated by Django 4.1 on 2022-09-02 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailer', '0002_trailer_category_trailer_manufacturer_trailer_qty_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trailerinterior',
            name='treshold_plate',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]