# Generated by Django 2.2.6 on 2019-10-16 08:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('medline', '0009_auto_20191016_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consult',
            name='reserve_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]