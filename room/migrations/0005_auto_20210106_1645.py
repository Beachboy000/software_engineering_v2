# Generated by Django 3.1.4 on 2021-01-06 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_auto_20210106_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 6, 16, 45, 4, 40918)),
        ),
    ]
