from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime, secrets
from .values import *
from .models import Contact, Bookings


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #userType = forms.CharField(label='Account Type: ', widget=forms.Select(choices=USER_TYPES), required=False)
    mobile = forms.IntegerField(label='Mobile: ', required=False)
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

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'mobile', 'address', 'birthdate']

    def save(self, commit=True):
        User = super(UserRegisterForm, self).save(commit=False)
        #User.userType = self.cleaned_data["userType"]
        if commit:
            User.save()
        return User


class contactForm(forms.ModelForm):
    class Meta: #metadata for the contact form
        model = Contact
     # for the model form, use the Contact model
    #subject = forms.CharField(label = 'Subject', max_length=100, required=False)
    #message = forms.CharField(label = 'Message',widget=forms.Textarea, required=False)
        fields = ['user_name', 'first_name', 'last_name', 'age', 'email', 'message']


class UserBookingForm(forms.ModelForm):

    SINGLE, RETURN = 'single', 'return'
    TYPE_CHOICES = [
    (SINGLE, 'Single'),
    (RETURN, 'Return')
    ]

    startlocation = forms.CharField(label='Starting From: ',
                                    widget=forms.Select(choices=STARTCITY_CHOICES),
                                    required=False)
    destination = forms.CharField(label='Destination: ', widget=forms.Select(choices=DESTINATION_CHOICES), required=False)
    departuretime = forms.TimeField(label='Time: ', widget=forms.Select(choices=TIME_CHOICES), required=False)
    journeydate = forms.DateField(label='Date: ',
                                  widget=forms.TextInput(
                                    attrs={'type': 'date'}
                                  ),
                                  initial = {'journeydate': datetime.date.today},
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

    class Meta:
        model = Bookings
        fields = ['startlocation', 'destination', 'journeydate', 'departuretime', 'journeytype', 'numberoftickets']

    def __init__(self, data=None, *args, **kwargs):
        super(UserBookingForm, self).__init__(data, *args, **kwargs)
        self.initial['journeydate'] = datetime.date.today

        if data and data.get('journeytype', None) == self.RETURN:
            returndate = forms.DateField(label='Date: ',
                            widget=forms.TextInput(
                                attrs={'type': 'date'}
                                ),
                                required=False
                            )

    def save(self, commit=True):
        Booking = super(UserBookingForm, self).save(commit=False)
        if commit:
            Booking.save()
        return Booking

#class CreditCardField(forms.IntegerField):
