from .models import Trips

STARTCITY_CHOICES = [(trip.startlocation, trip.startlocation) for trip in Trips.objects.distinct()]
DESTINATION_CHOICES = [(trip.destination, trip.destination) for trip in Trips.objects.distinct()]
TIME_CHOICES = [(trip.departuretime, trip.departuretime) for trip in Trips.objects.distinct()]

USER_TYPES = [
('Ad', 'Adult'),
('Ch', 'Child'),
('Ret', 'Retired'),
('Student', 'Student'),
]
