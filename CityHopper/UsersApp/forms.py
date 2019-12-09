from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime, secrets
from .values import *
from .models import Contact, Bookings

#Creating a user registeration from and inheriting the UserCreationForm
class UserRegisterForm(UserCreationForm):
    #Adding custom fields for the user to input
    email = forms.EmailField()
    mobile = forms.IntegerField(label='Mobile: ', required=False)
    #birthdate taken as input with validation
    birthdate = forms.DateField(label='Birth Date: ',
                                widget=forms.TextInput(
                                            attrs={'type': 'date'}
                                        ),
                                initial = datetime.date.today,
                                validators = [
                                    MaxValueValidator(datetime.date.today)
                                    ],
                                required=True

                    )
    address = forms.CharField()

    #Maps the form to the user model
    class Meta:
        #Specify the model to map to
        model = User
        #Specify the fields to map to
        fields = ['username',
                  'email',
                  'password1',
                  'password2',
                  'mobile',
                  'address',
                  'birthdate']

    #A function to clean form data
    def clean(self):
        cd = self.cleaned_data
        cd.customer = request.user
        return cd

    #A function to save form data and transfer to views
    def save(self, commit=True):
        User = super(UserRegisterForm, self).save(commit=False)
        #User.userType = self.cleaned_data["userType"]
        if commit:
            User.save()
        return User

#Creating a user contact from. It is a model from which is generated from and mapped back to a model
class contactForm(forms.ModelForm):

    class Meta:
        #The model to gereate from and map to
        model = Contact
        #Fields to be used
        fields = ['user_name',
                  'first_name',
                  'last_name',
                  'age',
                  'email',
                  'message']

#The booking form generated from the booking model and with custom fields
class UserBookingForm(forms.ModelForm):

    #Dictionary object for 'Journey Type' field
    SINGLE, RETURN = 'single', 'return'
    TYPE_CHOICES = [
    (SINGLE, 'Single'),
    (RETURN, 'Return')
    ]

    def is_NotEqual(start, end):
            return start == end

    #Choice fields in this form use objects generated at run time directly from the DB (Objects are in values.py)
    #start location field
    startlocation = forms.CharField(label='Starting From: ',
                                    widget=forms.Select(choices=STARTCITY_CHOICES),
                                    required=False)
    #destination field
    destination = forms.CharField(label='Destination: ',
                                  widget=forms.Select(choices=DESTINATION_CHOICES),
                                  required=False)
    def clean_test_value(self):
        start = self.cleaned_data.get('startlocation')
        end = self.cleaned_data.get('destination')

        if is_NotEqual(start, end):
            raise forms.ValidationError('From and To cannot be the same city!')

    #departure time field
    departuretime = forms.TimeField(label='Time: ',
                                    widget=forms.Select(choices=TIME_CHOICES),
                                    required=False)
    #journey date field (Uses a date picker and validates date)
    journeydate = forms.DateField(label='Date: ',
                                  widget=forms.TextInput(
                                                    attrs={'type': 'date'}
                                                    ),
                                  initial = datetime.date.today,
                                  validators = [
                                    MinValueValidator(datetime.date.today)
                                  ],
                                  required=False)
    #journey type field
    journeytype = forms.CharField(label='Journey Type: ',
                                  widget=forms.Select(choices=TYPE_CHOICES),
                                  required=False)
    #number of tickets field with max validation
    numberoftickets = forms.IntegerField(
                                      label='No. of Tickets (Max 5): ',
                                      widget=forms.TextInput(),
                                      required=False,
                                      initial=1,
                                      validators=[
                                        MaxValueValidator(5),
                                        MinValueValidator(1)
                                      ])
    #customer field is hidden and populated during form.save() with the current user
    customer = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        #The model to gereate from and map to
        model = Bookings
        #Fields to be used
        fields = ['startlocation',
                  'destination',
                  'journeydate',
                  'departuretime',
                  'journeytype',
                  'numberoftickets',
                  'customer']

    #Populating date field with initial value (Today)
    def __init__(self, data=None, *args, **kwargs):
        super(UserBookingForm, self).__init__(data, *args, **kwargs)
        self.initial['journeydate'] = datetime.date.today

    #Function to save the form data and transfer to views
    def save(self, commit=True):
        Booking = super(UserBookingForm, self).save(commit=False)
        if commit:
            Booking.save()
        return Booking
