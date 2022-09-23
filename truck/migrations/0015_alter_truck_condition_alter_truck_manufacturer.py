# Generated by Django 4.1 on 2022-09-03 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('truck_utils', '0007_alter_truckcategory_parent'),
        ('truck', '0014_alter_truck_listing_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='condition',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='condition_trucks', to='truck_utils.condition'),
        ),
        migrations.AlterField(
            model_name='truck',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manufacturer_trucks', to='truck_utils.truckmanufacturer'),
        ),
    ]