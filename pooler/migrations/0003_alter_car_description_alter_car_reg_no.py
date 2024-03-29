# Generated by Django 4.1.4 on 2023-01-05 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pooler', '0002_alter_car_reg_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='car',
            name='reg_no',
            field=models.CharField(max_length=20, unique=True, verbose_name='Registration Number'),
        ),
    ]
