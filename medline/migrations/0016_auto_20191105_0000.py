# Generated by Django 2.2.6 on 2019-11-04 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medline', '0015_auto_20191104_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescribedmedicine',
            name='prescription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medline.Prescription'),
        ),
    ]