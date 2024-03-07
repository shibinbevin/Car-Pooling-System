# Generated by Django 4.1.4 on 2023-01-24 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pooler', '0003_alter_car_description_alter_car_reg_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('origin', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('departure_time', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.BooleanField(default=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pooler.car')),
            ],
        ),
        migrations.CreateModel(
            name='WayPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(max_length=255)),
                ('km', models.FloatField()),
                ('expected_time', models.TimeField()),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pooler.ride')),
            ],
        ),
    ]
