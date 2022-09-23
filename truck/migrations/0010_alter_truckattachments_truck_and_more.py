# Generated by Django 4.1 on 2022-09-03 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0009_alter_truckattachments_truck_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truckattachments',
            name='truck',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='truck_attachments', to='truck.truck'),
        ),
        migrations.AlterField(
            model_name='truckcapacities',
            name='truck',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='truck_capacities', to='truck.truck'),
        ),
        migrations.AlterField(
            model_name='truckcategoryspecific',
            name='truck',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='truck_category_specific', to='truck.truck'),
        ),
        migrations.AlterField(
            model_name='truckdimensions',
            name='truck',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='truck_dimensions', to='truck.truck'),
        ),
        migrations.AlterField(
            model_name='truckexterior',
            name='truck',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='truck_exterior', to='truck.truck'),
        ),
        migrations.AlterField(
            model_name='truckpowertrain',
            name='ratio',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]