from django.shortcuts import render
from UsersApp.models import Trips
#This is where we define all our views for the MTV pattern (MVC)

#Home page
def index(request):
    context = {
        'trips': Trips.objects.all(),
    }
    #returns an html page to render
    return render(request, 'cityhopper/home.html', context)

#About page
def about(request):
    #returns an html page to render
    return render(request, 'cityhopper/about.html')
