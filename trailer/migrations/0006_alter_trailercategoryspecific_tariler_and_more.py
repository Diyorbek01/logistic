# Generated by Django 4.1 on 2022-09-04 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trailer', '0005_alter_trailercategoryspecific_tariler_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailercategoryspecific',
            name='tariler',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trailer_category_specific', to='trailer.trailer'),
        ),
        migrations.AlterField(
            model_name='trailerchassis',
            name='trailer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trailer_chassis', to='trailer.trailer'),
        ),
        migrations.AlterField(
            model_name='trailerdimensions',
            name='trailer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trailer_dimensions', to='trailer.trailer'),
        ),
        migrations.AlterField(
            model_name='trailerexterior',
            name='trailer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trailer_exterior', to='trailer.trailer'),
        ),
        migrations.AlterField(
            model_name='trailerinterior',
            name='trailer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trailer_interior', to='trailer.trailer'),
        ),
        migrations.CreateModel(
            name='TrailerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='trailer-images/')),
                ('trailer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trailer_images', to='trailer.trailer')),
            ],
        ),
    ]