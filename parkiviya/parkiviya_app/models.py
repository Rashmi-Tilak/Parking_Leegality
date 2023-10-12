from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import User, AbstractUser
# Create your models here.
from django.db import models
# Create your models here.

# class CustomUser(AbstractUser, PermissionsMixin):
#
#     phone_number = models.CharField(max_length=20, blank=True)
#     is_verified = models.BooleanField(default=False)
#     username = models.CharField(max_length=150, unique=True, null=True, blank=False)
#     email = models.EmailField(unique=True, blank=False)
#     address = models.TextField(max_length=250, blank=False)
#     otp = models.CharField(max_length=20, blank=True, null=True)
#     is_logged_in = models.BooleanField(default=False)
#
#
#     objects = CustomUserManager()
#
#     # Use 'phone_number' as the unique identifier for authentication
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['phone_number']
#
#     class Meta:
#         db_table = 'parkiviya_customuser'

class ParkingSpot(models.Model):
    level = models.CharField(max_length=1, choices=[('A', 'Level A'), ('B', 'Level B')])
    spot_number = models.IntegerField(unique=True)
    vehicle_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.level} - {self.spot_number}"

    class Meta:
        db_table = 'parkingspot'
