from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Trips
from .forms import UserRegisterForm, UserBookingForm,contactForm
from django.core.mail import send_mail # forms
from django.core.mail import send_mail, BadHeaderError

from django.http import HttpResponse, HttpResponseRedirect


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

def profile(request):
    return render(request, 'users/profile.html')

def timetable(request):
    context = {
        'trips' : Trips.objects.all()
    }
    return render(request, 'users/timetable.html', context)

def booktickets(request):
    form_class = UserBookingForm
    form = form_class(request.POST)
    context = {
        'trips' : Trips.objects.all(),
        'form'  : form
    }
    if request.method == 'POST':
        form = UserBookingForm(request.POST)
        if form.is_valid():
            form.save()
            startlocation = form.cleaned_data.get('startlocation')
            destination = form.cleaned_data.get('destination')
            starttime= form.cleaned_data.get('starttime')
            journeydate = form.cleaned_data.get('journeydate')
            journeytype = form.cleaned_data.get('journeytype')
            numberoftickets = form.cleaned_data.get('numberoftickets')
            messages.success(request, f'Booking request recorded successfully: from {startlocation} to {destination} at {starttime} on {journeydate} - {journeytype} for {numberoftickets} people.')
            return redirect('cityhopper-booking')
        else:
            form = UserBookingForm()
    return render(request, 'users/bookticket.html', context)

def home(request):
    context = {
        'trips' : Trips.objects.all()
    }
    return render(request, 'users/home.html', context)

def contact(request):
    form_class = contactForm
    form = form_class(request.POST)
    context = {

        'form'  : form
    }

    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data.get('Subject')
            message = form.cleaned_data.get('Message')
            messages.success(request, f'Query recorded successfully! We will contact you within 24 hours!')
            return redirect('cityhopper-contact')
        else:
            form = UserBookingForm()
    return render(request, 'users/contact.html', context)

    #return render(request, 'users/contact.html', {'form': form})

def offers(request):
    return render(request, 'users/offers.html')

def news(request):
    return render(request, 'users/news.html')



    #message.debug
    #message.info
    #message.success
    #message.warning
