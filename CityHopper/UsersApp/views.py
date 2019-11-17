from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserBookingForm


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

def booktickets(request):
    form_class = UserBookingForm
    form = form_class(request.POST)
    if request.method == 'POST':
        form = UserBookingForm(request.POST)
        if form.is_valid():
            form.save()
            startlocation = form.cleaned_data.get('startlocation')
            destination = form.cleaned_data.get('destination')
            starttime= form.cleaned_data.get('starttime')
            journeydate = form.cleaned_data.get('journeydate')
            journeytype = form.cleaned_data.get('journeytype')
            messages.success(request, f'Booking request recorded successfully: {startlocation} {destination} {starttime} {journeydate} {journeytype}')
            return redirect('cityhopper-booking')
        else:
            form = UserBookingForm()
    return render(request, 'users/bookticket.html', {'form': form})


    #message.debug
    #message.info
    #message.success
    #message.warning
