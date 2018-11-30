# Generated by Django 2.1.3 on 2018-11-29 18:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nightmare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nightmare',
            name='date_creation',
            field=models.DateField(default=datetime.datetime(2018, 11, 29, 18, 11, 53, 113105, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='nightmarepart',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='nightmare_part/'),
        ),
    ]