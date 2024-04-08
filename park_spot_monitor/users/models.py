from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Plates(models.Model):
    plate = models.CharField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.plate}"
    

class Sessions(models.Model):
    entrance_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True)
    plate = models.ForeignKey(Plates, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class Entry(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100)  # Ви можете налаштувати це поле відповідно до вашого використання

    def __str__(self):
        return f"{self.datetime} - {self.type}"


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username} - ${self.amount}"

@receiver(post_save, sender=User)
def create_or_update_balance(sender, instance, created, **kwargs):
    if created:
        Balance.objects.create(user=instance)
    else:
        instance.balance.amount = 0  # Передбачаємо, що balance має атрибут amount
        instance.balance.save()
