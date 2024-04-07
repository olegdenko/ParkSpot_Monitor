from django.db import models

# Create your models here.
# models.py

from django.db import models

class RegisteredNumberPlate(models.Model):
    plate_number = models.CharField(max_length=20, unique=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.plate_number


class ParkingRate(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class BlacklistedVehicle(models.Model):
    plate_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.plate_number
