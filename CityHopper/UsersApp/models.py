from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import datetime, uuid

#Default ID primary key is created for each model

#Model profile that extends the user and has a one to one mapping.
#Thus each entry in the user model will have only one corresponding entry in the
#Profile tabel and vica-versa.
class Profile(models.Model):
    #The one to one mapper. If a user is deleted, their profile is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image for the user
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    #Mobile number
    mobile = models.IntegerField(default = 65656565)
    #userType of the user (Student, Adult etc)
    userTypes = models.TextField(default='default')
    #birthdate field
    birthdate = models.DateField(default = datetime.date.today)

    #When we call objects through cmd, it will return the below as a string
    def __str__(self):
        #Using F strings from python to print custom strings
        return f'{self.user.username} Profile'

#Contact model to store all messages into DB
class Contact(models.Model):
    user_name = models.CharField(max_length=50, default ='')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    age = models.IntegerField(default =18)

    #When we call objects through cmd, it will return the below as a string
    def __str__(self):
        #Using F strings from python to print custom strings
        return f'{self.first_name} {self.last_name}'

#The main booking model.
class Bookings(models.Model):
    #Bookingid is the primary key and a unique hex code
    bookingid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False, unique=True)
    #Customer stores the user credentials to making a booking specific to a user
    customer = models.CharField(max_length=100)
    startlocation = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    journeydate = models.DateField()
    departuretime = models.TimeField()
    journeytype = models.CharField(max_length=100)
    numberoftickets = models.IntegerField()

    #When we call objects through cmd, it will return the below as a string
    def __str__(self):
        #Using F strings from python to print custom strings
        return f'{self.bookingid}, {self.customer}, {self.startlocation}, {self.destination}, {self.journeydate}, {self.departuretime}'

#Trips table store all the Trips
#Table is used by TimeTable to generate the page at runtime
#Tbale is also used to generate form choices dynamically at runtime for booking
class Trips(models.Model):
    busID = models.IntegerField() #Ideally Foreign Key
    startlocation = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departuretime = models.TimeField()
    duration = models.CharField(max_length=100)
    #price is stored as amount+00 due to Stripe requirements
    price = models.IntegerField()
