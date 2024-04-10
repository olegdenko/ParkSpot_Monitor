from django.db import models
from django.contrib.auth.models import User


class Plates(models.Model):
    plate = models.CharField(unique=True, max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.plate} User {self.user.username}"


class Sessions(models.Model):
    entrance_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True)
    plate = models.ForeignKey(Plates, on_delete=models.CASCADE)

    def __str__(self):
        return f"Session for {self.plate.plate}"

# class BlacklistedVehicle(models.Model):
#     plate = models.ForeignKey('Plates', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.plate.plate} User {self.user.username}"
