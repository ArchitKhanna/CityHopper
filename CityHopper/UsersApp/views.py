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
            #messages.success(request, f'Account created successfully!')
            return redirect('#')
        else:
            form = UserBookingForm()
    return render(request, 'users/bookticket.html', {'form': form})


    #message.debug
    #message.info
    #message.success
    #message.warning
