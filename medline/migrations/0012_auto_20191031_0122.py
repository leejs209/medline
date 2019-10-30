# Generated by Django 2.2.6 on 2019-10-30 16:22

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('medline', '0011_prescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consult',
            name='symptoms',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('a1', '복통'), ('a2', '외상'), ('a3', '두통'), ('a4', '어지로움')], max_length=30),
        ),
    ]
