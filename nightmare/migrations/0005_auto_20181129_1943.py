# Generated by Django 2.1.3 on 2018-11-29 18:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nightmare', '0004_auto_20181129_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nightmare',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2018, 11, 29, 18, 43, 13, 682888, tzinfo=utc)),
        ),
    ]