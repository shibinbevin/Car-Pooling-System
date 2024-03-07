from django.db import models
from accounts.models import Pooler

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Category'
    )
    def __str__(self):
        return self.name

class Car(models.Model):
    reg_no = models.CharField(
        max_length=20,
        verbose_name='Registration Number',
        unique=True
    )
    description = models.TextField(
        max_length=300,
        verbose_name='Description',
        null=True,
        blank=True
    )
    image = models.FileField(
        upload_to='Vehicle',
        max_length=300
    )
    capacity = models.IntegerField(
        verbose_name='Passanger Capacity',
        default=3,
        editable=False
    )
    luggage_capacity = models.IntegerField(
        verbose_name='Luggage Capacity'
    )
    air_condition = models.BooleanField(
        default=False,
        verbose_name='A/C Status'
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE
    )
    status = models.BooleanField(
        default=True
    )
    owner = models.ForeignKey(
        to=Pooler,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.reg_no

import datetime
class Ride(models.Model):
    car = models.ForeignKey(
        to=Car,
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    estimated_reaching_time = models.DateTimeField(default=datetime.datetime.now())
    gender_preference = models.IntegerField(choices=((0, "Male Only"), (1, "Female Only"), (2, "No Preference")), default=2)
    description = models.TextField(default='', null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

class WayPoint(models.Model):
    point = models.CharField(max_length=255)
    km = models.FloatField()
    ride = models.ForeignKey(to=Ride, on_delete=models.CASCADE)