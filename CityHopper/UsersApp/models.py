from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    mobile = models.IntegerField(default = 0000000)
    userTypes = models.TextField(default='default')

    def __str__(self):
        return f'{self.user.username} Profile'

"""class Bookings(models.Model):
    startinglocation = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    journeydate = models.DateField()
    starttime = models.TimeField()
    journeytype = models.CharField(max_length=100)
    numberoftickets = models.IntegerField()"""

class Trips(models.Model):
    #tripID = models.IntegerField() //Default ID is created for each model
    busID = models.IntegerField() #Ideally Foreign Key
    startlocation = models.TextField()
    destination = models.TextField()
    departuretime = models.TimeField()
    duration = models.TextField()
    #arrivaltime=models.TextField()
    price = models.IntegerField()
