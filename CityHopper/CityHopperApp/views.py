from django.shortcuts import render
#This is where we define all our views for the MTV pattern (MVC)

#Home page
def index(request):
    #returns an html page to render
    return render(request, 'cityhopper/index.html')

#About page
def about(request):
    #returns an html page to render
    return render(request, 'cityhopper/about.html')
