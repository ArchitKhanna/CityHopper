from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import datetime, uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    mobile = models.IntegerField(default = 65656565)
    userTypes = models.TextField(default='default')
    birthdate = models.DateField(default = datetime.date.today)

    def __str__(self):
        return f'{self.user.username} Profile'

class Contact(models.Model):
    user_name = models.CharField(max_length=50, default ='')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    age = models.IntegerField(default =18)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Bookings(models.Model):
    bookingid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    startlocation = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    journeydate = models.DateField()
    departuretime = models.TimeField()
    journeytype = models.CharField(max_length=100)
    numberoftickets = models.IntegerField()

class Trips(models.Model):
    #tripID = models.IntegerField() //Default ID is created for each model
    busID = models.IntegerField() #Ideally Foreign Key
    startlocation = models.TextField()
    destination = models.TextField()
    departuretime = models.TimeField()
    duration = models.TextField()
    #arrivaltime=models.TextField()
    price = models.IntegerField()
