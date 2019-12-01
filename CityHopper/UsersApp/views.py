from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Trips, Profile, Bookings
from .decorators import superuser_only
from .forms import UserRegisterForm, UserBookingForm,contactForm
from django.core.mail import send_mail # forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import secrets
from django.conf import settings #stripe
from django.views.generic.base import TemplateView #stripe
import stripe #stripe

#API aithentication key for Stripe Payments
stripe.api_key = settings.STRIPE_SECRET_KEY

#Creating a custom view for user registration
def register(request):
    #Depending on the type of request, the actiion can be modified.
    #If its a POST request then process the data sent else render the page
    if request.method == 'POST':
        #creates an instance of the form submitted with data
        form = UserRegisterForm(request.POST)
        #Form validation
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #Response message for better user experience
            messages.success(request, f'Account created successfully!')
            return redirect('login')
    else:
        #creates an instance of the form
        form = UserRegisterForm()
    #Renders the HTML page and passes a variable request and the forms
    return render(request, 'users/register.html', {'form': form})


#Login decorator that checks if a user is logged in. If not then the user is redirected to login
@login_required(login_url='/login/')
#Creating a custom view for user profile
def profile(request):
    #context is a dictionary of variables that can be passed to render
    context = {
        'profile' : Profile.objects.all()
    }
    return render(request, 'users/profile.html', context)


#Login decorator that checks if a user is logged in. If not then the user is redirected to login
@login_required(login_url='/login/')
#Creating a custom view for timetable
def timetable(request):
    #context is a dictionary of variables that can be passed to render
    context = {
        'trips' : Trips.objects.all()
    }
    return render(request, 'users/timetable.html', context)

#Login decorator that checks if a user is logged in. If not then the user is redirected to login
@login_required(login_url='/login/')
#Creating a custom view for booking form
def booktickets(request):
    form_class = UserBookingForm
    form = form_class(request.POST)
    #context is a dictionary of variables that can be passed to render
    context = {
        'trips' : Trips.objects.all(),
        'form'  : form
    }
    if request.method == 'POST':
        #creates an instance of the form submitted with data
        form = UserBookingForm(request.POST)
        #Connecting the user to the booking through session variables
        form.data._mutable = True
        form.data['customer'] = request.user
        #Form validation
        if form.is_valid():
            form.save()
            #Setting variables with form data for acknowledgement message
            customer = form.cleaned_data.get('customer')
            startlocation = form.cleaned_data.get('startlocation')
            destination = form.cleaned_data.get('destination')
            departuretime= form.cleaned_data.get('departuretime')
            journeydate = form.cleaned_data.get('journeydate')
            journeytype = form.cleaned_data.get('journeytype')
            numberoftickets = form.cleaned_data.get('numberoftickets')
            #Acknowldement message for better User Experience
            messages.success(request, f'Hi {customer}! Booking request : from {startlocation} to {destination} at {departuretime} on {journeydate} - {journeytype} for {numberoftickets} people will be confirmed upon receipt of payment.')
            return redirect('cityhopper-payment')
        else:
            #creates an instance of the form
            form = UserBookingForm()
    #Renders the HTML page and passes a variable request and the forms
    return render(request, 'users/bookticket.html', context)

#Login decorator that checks if a user is logged in. If not then the user is redirected to login
@login_required(login_url='/login/')
def home(request):
    #context is a dictionary of variables that can be passed to render
    context = {
        'trips' : Trips.objects.all()
    }
    return render(request, 'users/home.html', context)

#Login decorator that checks if a user is logged in. If not then the user is redirected to login
@login_required(login_url='/login/')
def contact(request):

    templates = "users/contact.html"

    if request.method == 'POST':
        #New instance of the form with data
        form = contactForm(request.POST)
        #form validation
        if form.is_valid():
            #Saving the form
            form.save()
            #Acknowldgement message
            messages.success(request, f'Query recorded successfully! We will contact you within 24 hours!')
            return redirect('cityhopper-contact')
    else:
        form = contactForm()

    #context is a dictionary of variables that can be passed to render
    context = {
    'form': form,
    }

    return render(request, templates, context)

#Login decorator that checks if a user is logged in. If not then the user is redirected to login
@login_required(login_url='/login/')
def offers(request):
    return render(request, 'users/offers.html')

#Login decorator that checks if a user is logged in. If not then the user is redirected to login
@login_required(login_url='/login/')
def news(request):
    return render(request, 'users/news.html')

#Login decorator that checks if a user is logged in. If not then the user is redirected to login
@login_required(login_url='/login/')
#Layered decorator for restricted access - Only superusers can access the admin page
@superuser_only
def adminLink(request):
    return render(request, 'users/adminLink.html')

#Login decorator that checks if a user is logged in. If not then the user is redirected to login
@login_required(login_url='/login/')
def qr(request):
    #context is a dictionary of variables that can be passed to render
    context = {
        'bookings': Bookings.objects.all(),
    }
    return render(request, 'users/qr.html')


#stripe view has to be a class view
class payment(TemplateView):
    template_name = 'users/payment.html'
    #pass the publishable key to stripe so as to include payment in logs otherwise it wont accept the token and pass the info
    def get_context_data(self, **kwargs):
        dataKey = super().get_context_data(**kwargs)
        #Key comes in from Settings
        dataKey['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return dataKey



def paymentConfirmation(request):
    user = request.user
    context = {
        'bookings': Bookings.objects.all().filter(customer=user),
    }
    cost=Trips.objects.get(id=11).price
    if request.method == 'POST':
        payment = stripe.Charge.create(
        amount=cost,
        currency='eur',
        description='Cityhopper',
        source=request.POST['stripeToken']
        )
        return render(request, 'users/paymentConfirmation.html', context)
