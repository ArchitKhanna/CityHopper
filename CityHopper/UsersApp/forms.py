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
    #bookingcode = secrets.token_hex(5)
    class Meta:
        model = Bookings
        fields = ['startlocation', 'destination', 'journeydate', 'departuretime', 'journeytype', 'numberoftickets', 'bookingcode']

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
        Booking = super(UserBookingForm, self).save(commit=False)
        #User.userType = self.cleaned_data["userType"]
        if commit:
            Booking.save()
        return Booking

class CreditCardField(forms.IntegerField):
  def get_cc_type(self, number):

    number = str(number)
    #group checking by ascending length of number
    if len(number) == 13:
      if number[0] == "4":
        return "Visa"
    elif len(number) == 14:
      if number[:2] == "36":
        return "MasterCard"
    elif len(number) == 15:
      if number[:2] in ("34", "37"):
        return "American Express"
    elif len(number) == 16:
      if number[:4] == "6011":
        return "Discover"
      if number[:2] in ("51", "52", "53", "54", "55"):
        return "MasterCard"
      if number[0] == "4":
        return "Visa"
    return "Unknown"

  def clean(self, value):
    """Check if given CC number is valid and one of the
    card types we accept"""
    if value and (len(value) < 13 or len(value) > 16):
      raise forms.ValidationError("Please enter in a valid "+\
          "credit card number.")
    elif self.get_cc_type(value) not in ("Visa", "MasterCard",
        "American Express", "Discover"):

      raise forms.ValidationError("Please enter in a Visa, "+\
          "Master Card, Discover, or American Express credit card number.")

    return super(CreditCardField, self).clean(value)

class PaymentForm(forms.Form):
  number = CreditCardField(required = True, label = "Card Number")
  first_name = forms.CharField(required=True, label="Card Holder First Name", max_length=30)
  last_name = forms.CharField(required=True, label="Card Holder Last Name", max_length=30)
  expire_month = forms.IntegerField(required=True, label = "Expiry month", max_value = 12, widget = forms.TextInput(attrs={'size': '4'})),
  expire_year = forms.IntegerField(required=True, label = "Expiry year", max_value = 9999, widget = forms.TextInput(attrs={'size': '4'})),
  cvv_number = forms.IntegerField(required = True, label = "CVV Number",
      max_value = 9999, widget = forms.TextInput(attrs={'size': '4'}))

  def __init__(self, *args, **kwargs):
    self.payment_data = kwargs.pop('payment_data', None)
    super(PaymentForm, self).__init__(*args, **kwargs)

  def clean(self):
    cleaned_data = super(PaymentForm, self).clean()
    expire_month = cleaned_data.get('expire_month')
    expire_year = cleaned_data.get('expire_year')

    if expire_year in forms.fields.EMPTY_VALUES:
      #raise forms.ValidationError("You must select a valid Expiration year.")
      self._errors["expire_year"] = self.error_class(["You must select a valid Expiration year."])
      del cleaned_data["expire_year"]
    if expire_month in forms.fields.EMPTY_VALUES:
      #raise forms.ValidationError("You must select a valid Expiration month.")
      self._errors["expire_month"] = self.error_class(["You must select a valid Expiration month."])
      del cleaned_data["expire_month"]
    year = int(expire_year)
    month = int(expire_month)
    # find last day of the month
    day = monthrange(year, month)[1]
    expire = date(year, month, day)

    if date.today() > expire:
      #raise forms.ValidationError("The expiration date you entered is in the past.")
      self._errors["expire_year"] = self.error_class(["The expiration date you entered is in the past."])

    return cleaned_data
