# Generated by Django 4.1.4 on 2023-02-01 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pooler', '0012_alter_ride_estimated_reaching_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='estimated_reaching_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 1, 17, 15, 21, 289078)),
        ),
    ]