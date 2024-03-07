from django.db import models
from pooler.models import Ride
from accounts.models import UserExtra

# Create your models here.


class Booking(models.Model):
    ride = models.ForeignKey(
        to=Ride,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=UserExtra,
        on_delete=models.CASCADE
    )
    source = models.CharField(
        max_length=100,
        default=''
    )
    destination = models.CharField(
        max_length=100,
        default=''
    )
    seat = models.CharField(
        max_length=10,
        default=''
    )
    total_km = models.FloatField(
        default=0.0
    )
    amount = models.FloatField(
        default=0.0
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(
        default=0
    )