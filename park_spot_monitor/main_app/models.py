from django.db import models
from django.contrib.auth.models import User


class Plates(models.Model):
    plate = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='main_app_plates')

    class Meta:
        app_label = 'main_app'

    def __str__(self):
        return self.plate


class Sessions(models.Model):
    entrance_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True)
    plate = models.ForeignKey(Plates, on_delete=models.CASCADE)

    def __str__(self):
        return f"Session for {self.plate} at {self.entrance_time}"
