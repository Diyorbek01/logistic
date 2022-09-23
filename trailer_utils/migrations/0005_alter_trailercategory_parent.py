# Generated by Django 4.1 on 2022-09-06 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trailer_utils', '0004_alter_trailercategory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailercategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='trailer_utils.trailercategory'),
        ),
    ]
