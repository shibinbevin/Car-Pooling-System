from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(
        max_length=10,
        unique=True,
        null=False,
        blank=False
    )

    def __str__(self) -> str:
        return super().__str__()

class State(models.Model):
    state = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.state

class UserExtra(models.Model):
    ID_TYPE = (
        (0, "Aadhar"),
        (1, "Election ID"),
        (2, "Pan Card"),
        (3, "License")
    )
    id_type = models.IntegerField(
        choices=ID_TYPE
    )
    id_number=models.CharField(
        verbose_name="ID Number",
        max_length=20
    )
    city = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    zip_code = models.IntegerField(
        verbose_name="Zip Code"
    )
    state = models.ForeignKey(
        to='State',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to='User',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.user.username

class Pooler(models.Model):
    license=models.ImageField(
        verbose_name="License",
        upload_to='License',
        max_length=100
    )
    city = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    zip_code = models.IntegerField(
        verbose_name="Zip Code"
    )
    state = models.ForeignKey(
        to='State',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to='User',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


