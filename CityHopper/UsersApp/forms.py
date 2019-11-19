from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from .values import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserBookingForm(forms.Form):

    SINGLE, RETURN = 'single', 'return'
    TYPE_CHOICES = [
    (SINGLE, 'Single'),
    (RETURN, 'Return')
    ]

    startlocation = forms.CharField(label='Starting From: ', widget=forms.Select(choices=STARTCITY_CHOICES), required=False)
    destination = forms.CharField(label='Destination: ', widget=forms.Select(choices=DESTINATION_CHOICES), required=False)
    starttime = forms.TimeField(label='Time: ', widget=forms.Select(choices=TIME_CHOICES), required=False)
    journeydate = forms.DateField(label='Date: ',
                                  widget=forms.TextInput(
                                    attrs={'type': 'date'}
                                  ),
                                  initial = datetime.date.today,
                                  validators = [
                                    MinValueValidator(datetime.date.today)
                                  ],
                                  required=False
                    )
    journeytype = forms.CharField(label='Journey Type: ', widget=forms.Select(choices=TYPE_CHOICES), required=False)
    numberoftickets = forms.IntegerField(
                                      label='No. of Tickets (Max 5): ',
                                      widget=forms.TextInput(),
                                      required=False,
                                      initial=1,
                                      validators=[
                                        MaxValueValidator(5),
                                        MinValueValidator(1)
                                      ])
    #class meta:
    #    model = Bookings
    #    fields = []

    def __init__(self, data=None, *args, **kwargs):
        super(UserBookingForm, self).__init__(data, *args, **kwargs)

        if data and data.get('journeytype', None) == self.RETURN:
            returndate = forms.DateField(label='Date: ',
                            widget=forms.TextInput(
                                attrs={'type': 'date'}
                                ),
                                required=False
                            )

    def save(self, commit=True):
        """startlocation = self.startlocation
        destination = self.destination
        starttime= self.starttime
        journeydate = self.journeydate
        journeytype = self.journeytype"""
