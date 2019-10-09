# Generated by Django 2.2.6 on 2019-10-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medline', '0003_consult_reserve_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='consult',
            name='status',
            field=models.CharField(choices=[('wait', '상담 예정'), ('done', '상담 완료'), ('expire', '기간 만료')], default='wait', max_length=6),
        ),
    ]
