from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Bookings(models.Model):
    startinglocation = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    journeydate = models.DateField()
    starttime = models.TimeField()
    journeytype = models.CharField(max_length=100)
    numberoftickets = models.IntegerField()
# Create your models here.
