from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    usdt_bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    main_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    



def __str__(self):
    return f"{self.user.username}'s Profile"