# Generated by Django 4.1 on 2022-09-03 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck_utils', '0005_alter_truckcategory_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
