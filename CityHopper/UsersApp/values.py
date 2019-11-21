from .models import Trips

"""STARTCITY_CHOICES = [
('limerick', 'Limerick'),
('galway', 'Galway'),
('dublin', 'Dublin'),
('cork', 'Cork'),
]"""

STARTCITY_CHOICES = [(trip.startlocation, trip.startlocation) for trip in Trips.objects.distinct()]
DESTINATION_CHOICES = [(trip.destination, trip.destination) for trip in Trips.objects.distinct()]
TIME_CHOICES = [(trip.departuretime, trip.departuretime) for trip in Trips.objects.distinct()]

"""DESTINATION_CHOICES = [
('limerick', 'Limerick'),
('galway', 'Galway'),
('dublin', 'Dublin'),
('cork', 'Cork'),
]"""

"""TIME_CHOICES = [
('10:00', '10:00'),
('11:00', '11:00'),
('12:00', '12:00'),
('13:00', '13:00'),
('14:00', '14:00'),
('15:00', '15:00'),
]"""

USER_TYPES = [
('Ad', 'Adult'),
('Ch', 'Child'),
('Ret', 'Retired'),
('Student', 'Student'),
]
