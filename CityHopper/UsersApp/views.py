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

stripe.api_key = settings.STRIPE_SECRET_KEY

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



@login_required(login_url='/login/')
def profile(request):
    context = {
        'profile' : Profile.objects.all()
    }
    return render(request, 'users/profile.html', context)



@login_required(login_url='/login/')
def timetable(request):
    context = {
        'trips' : Trips.objects.all()
    }
    return render(request, 'users/timetable.html', context)


@login_required(login_url='/login/')
def booktickets(request):
    form_class = UserBookingForm
    form = form_class(request.POST)
    context = {
        'trips' : Trips.objects.all(),
        'form'  : form
    }
    if request.method == 'POST':
        form = UserBookingForm(request.POST)
        form.data._mutable = True
        form.data['customer'] = request.user
        if form.is_valid():
            form.save()
            customer = form.cleaned_data.get('customer')
            startlocation = form.cleaned_data.get('startlocation')
            destination = form.cleaned_data.get('destination')
            departuretime= form.cleaned_data.get('departuretime')
            journeydate = form.cleaned_data.get('journeydate')
            journeytype = form.cleaned_data.get('journeytype')
            numberoftickets = form.cleaned_data.get('numberoftickets')
            messages.success(request, f'Hi {customer}! Booking request : from {startlocation} to {destination} at {departuretime} on {journeydate} - {journeytype} for {numberoftickets} people will be confirmed upon receipt of payment.')
            return redirect('cityhopper-payment')
        else:
            form = UserBookingForm()
    return render(request, 'users/bookticket.html', context)

@login_required(login_url='/login/')
def home(request):
    context = {
        'trips' : Trips.objects.all()
    }
    return render(request, 'users/home.html', context)

@login_required(login_url='/login/')


def contact(request):
    templates = "users/contact.html"


    if request.method == 'POST':
        form = contactForm(request.POST)

        if form.is_valid():
            form.save()
            #subject = form.cleaned_data.get('Subject')
            #message = form.cleaned_data.get('Message')
            messages.success(request, f'Query recorded successfully! We will contact you within 24 hours!')
            return redirect('cityhopper-contact')
    else:
        form = contactForm() #UserBookingForm()

    context = {
    'form': form,
    }

    return render(request, templates, context)


@login_required(login_url='/login/')
def offers(request):
    return render(request, 'users/offers.html')

@login_required(login_url='/login/')
def news(request):
    return render(request, 'users/news.html')

@login_required(login_url='/login/')
@superuser_only
def adminLink(request):
    return render(request, 'users/adminLink.html')

@login_required(login_url='/login/')
def qr(request):
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
        #takes key from settings!!

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
