from django.shortcuts import render

def index(request):
    return render(request, 'cityhopper/index.html')

def about(request):
    return render(request, 'cityhopper/about.html')
