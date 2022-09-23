# Generated by Django 4.1 on 2022-09-02 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0007_truckengine_engine_manufacturer_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='truckattachments',
            options={'verbose_name_plural': 'Truck attachments'},
        ),
        migrations.AlterModelOptions(
            name='truckcapacities',
            options={'verbose_name_plural': 'Truck capacities'},
        ),
        migrations.AlterModelOptions(
            name='truckchassis',
            options={'verbose_name_plural': 'Truck chassis'},
        ),
        migrations.AlterModelOptions(
            name='truckdimensions',
            options={'verbose_name_plural': 'Truck dimensions'},
        ),
        migrations.CreateModel(
            name='TruckImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='truck-images/')),
                ('truck', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='truck_images', to='truck.truck')),
            ],
        ),
    ]