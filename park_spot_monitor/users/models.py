from django.db import models
from django.contrib.auth.models import User


class Plates(models.Model):
    plate = models.CharField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.plate}"
    

class Sessions(models.Model):
    entrance_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True)
    plate = models.ForeignKey(Plates, on_delete=models.CASCADE)
