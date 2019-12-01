from .models import Trips

#Objects generated at runtime directly from Trips model
STARTCITY_CHOICES = [(trip.startlocation, trip.startlocation) for trip in Trips.objects.distinct()]
DESTINATION_CHOICES = [(trip.destination, trip.destination) for trip in Trips.objects.distinct()]
TIME_CHOICES = [(trip.departuretime, trip.departuretime) for trip in Trips.objects.distinct()]
